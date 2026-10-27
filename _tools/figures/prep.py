"""Preprocess a mod config with pcpp: python prep.py fza_ah64_mpd/config.cpp out.cpp

The mod's addons and include folders are mirrored into one root with forward-slash includes. Arma's preprocessor
groups [] and {} in macro arguments as well as (), so pcpp's argument collector is patched to do the same.
"""
import inspect
import io
import os
import re
import sys
import textwrap

import pcpp.preprocessor
from pcpp import Preprocessor

import paths

VROOT = os.path.join(paths.CACHE, 'vroot')
INC_RE = re.compile(r'^(\s*#\s*include\s*)["<]([^">]+)[">]', re.M)


def _patch_collect_args():
    src = textwrap.dedent(inspect.getsource(Preprocessor.collect_args))
    m = re.search(r"^( *)elif t\.value == '\)':", src, re.M)
    if not m:
        raise SystemExit('pcpp changed: cannot patch collect_args')
    ind, old = m.group(1), m.group(0)
    new = (ind + "elif t.value == '[' or t.value == '{':\n" + ind + "    current_arg.append(t)\n" + ind + "    nesting += 1\n"
           + ind + "elif t.value == ']' or t.value == '}':\n" + ind + "    current_arg.append(t)\n" + ind + "    nesting -= 1\n" + old)
    ns = {}
    exec(compile(src.replace(old, new, 1), 'collect_args', 'exec'), vars(pcpp.preprocessor), ns)
    Preprocessor.collect_args = ns['collect_args']


_patch_collect_args()


def mirror():
    if os.path.isdir(VROOT):
        return
    for base in ('addons', 'include'):
        src = paths.mod(base)
        for dp, dn, fn in os.walk(src):
            out = os.path.join(VROOT, os.path.relpath(dp, src))
            os.makedirs(out, exist_ok=True)
            for f in fn:
                if not f.lower().endswith(('.hpp', '.h', '.cpp', '.inc', '.sqf')):
                    continue
                s = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
                s = INC_RE.sub(lambda m: m.group(1) + '"' + m.group(2).replace('\\', '/').lstrip('/') + '"', s)
                open(os.path.join(out, f), 'w', encoding='utf-8').write(s)
    # version.hpp is written by HEMTT at build time
    for d in os.listdir(VROOT):
        v = os.path.join(VROOT, d, 'version.hpp')
        if os.path.isdir(os.path.join(VROOT, d)) and not os.path.exists(v):
            open(v, 'w').write('')


class P(Preprocessor):
    def on_error(self, file, line, msg):
        sys.stderr.write('ERR %s:%s %s\n' % (file, line, msg))

    def on_include_not_found(self, is_malformed, is_system_include, curdir, includepath):
        sys.stderr.write('MISSING %s (from %s)\n' % (includepath, curdir))
        raise self.OutputDirective(1)


def run(entry, out):
    mirror()
    p = P()
    p.add_path(VROOT)
    p.line_directive = None
    path = os.path.join(VROOT, entry)
    p.parse(open(path, encoding='utf-8').read(), path)
    buf = io.StringIO()
    p.write(buf)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(buf.getvalue())


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])

"""Where the figure tools find the mod and the docs.

FM_MOD: a checkout of the AH-64D mod at the commit being documented (required for anything that reads mod files).
FM_DOCS: the docs repo; defaults to the checkout this file is in.
"""
import json
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.environ.get('FM_DOCS', os.path.normpath(os.path.join(HERE, '..', '..')))
MOD = os.environ.get('FM_MOD', '')
CACHE = os.path.join(HERE, '.cache')
OUT = os.path.join(CACHE, 'out')
FONT = os.path.join(DOCS, 'assets', 'fonts', 'BMKApacheFont.ttf')


def mod(*parts):
    if not MOD:
        raise SystemExit('Set FM_MOD to a checkout of the AH-64D mod')
    return os.path.join(MOD, *parts)


def shoot(jobs):
    """Screenshot HTML files: [{'html', 'png', 'width', 'height', 'transparent'}]."""
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
        json.dump(jobs, f)
    try:
        subprocess.run(['node', os.path.join(HERE, 'shoot.js'), f.name], check=True)
    finally:
        os.unlink(f.name)

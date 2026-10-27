"""Render MPD page states to SVG, and to PNG for checking: python run.py states.json [name ...]"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import paths  # noqa: E402
import render  # noqa: E402

OUT = paths.OUT


def build(state, mfd, consts):
    off = render.MPD_OFFSET_L
    user, text = {}, {}
    for k, v in state.get('u', {}).items():
        idx = consts[k] if isinstance(k, str) and not k.isdigit() else int(k)
        user[idx + off] = v
    for k, v in state.get('t', {}).items():
        idx = consts[k] if isinstance(k, str) and not k.isdigit() else int(k)
        text[idx + off] = v
    for k, v in state.get('raw', {}).items():
        user[int(k)] = v
    page = consts['MPD_PAGE_' + state['page']] if isinstance(state['page'], str) else state['page']
    r = render.Renderer(mfd, user, text, state.get('src'))
    return r.render(page)


def to_png(svg_path, png_path, size=1000):
    html = svg_path[:-4] + '.html'
    open(html, 'w', encoding='utf-8').write(
        '<!doctype html><html><head><style>@font-face{font-family:"BMKApacheFont";src:url("file://%s")}'
        'html,body{margin:0;background:#000}</style></head><body>%s</body></html>'
        % (paths.FONT, open(svg_path, encoding='utf-8').read()))
    paths.shoot([{'html': html, 'png': png_path, 'width': size, 'height': size}])


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    mfd = render.load_mfd()
    consts = render.load_constants()
    states = json.load(open(sys.argv[1], encoding='utf-8'))
    only = sys.argv[2:] or list(states)
    for name in only:
        svg = build(states[name], mfd, consts)
        p = os.path.join(OUT, name + '.svg')
        open(p, 'w', encoding='utf-8').write(svg)
        to_png(p, p[:-4] + '.png')
        print('wrote', name)

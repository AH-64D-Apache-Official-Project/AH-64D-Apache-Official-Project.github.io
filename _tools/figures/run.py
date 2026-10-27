"""Render MPD page states to SVG, and to PNG for checking: python run.py states.json [name ...]"""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import paths  # noqa: E402
import render  # noqa: E402

OUT = paths.OUT


MAGS = []


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
    if state.get('pylons') and not MAGS:
        MAGS.append(render.load_mags())
    r = render.Renderer(mfd, user, text, state.get('src'), pylons=state.get('pylons'), mags=MAGS[0] if MAGS else None)
    svg = r.render(page)
    if state.get('fcr'):
        svg = svg.replace('\n</svg>', '\n' + fcr_symbols(state['fcr']) + '\n</svg>')
    return svg


# The FCR scope draws its symbols in the browser layer over the page (fza_ah64_fcr/ui/scope/scope.js): ownship
# centre and 8 km radius in display units, GTM wedge or ATM circle; sprites 0.09 of the display high
FCR_GEOM = {1: (0.5, 0.87, 0.65), 2: (0.5, 0.5, 0.325)}


def fcr_symbols(spec):
    import icons
    cx, cy, r8k = FCR_GEOM[spec.get('mode', 1)]
    size = 0.09 * render.S
    out = []
    for t in spec.get('targets', []):
        a, r = math.radians(t['a']), t['r'] / 8000.0
        x = (cx + math.sin(a) * r * r8k) * render.S - size / 2
        y = (cy - math.cos(a) * r * r8k) * render.S - size / 2
        for key in [t['icon']] + ([t['ov']] if t.get('ov') else []):
            out.append('<image x="%.1f" y="%.1f" width="%.1f" height="%.1f" href="%s"/>'
                       % (x, y, size, size, icons.data_uri(key, 0.5 if t.get('dim') else 1.0)))
    return '\n'.join(out)


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

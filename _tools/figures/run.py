"""Render MPD page states to SVG, and to PNG for checking: python run.py states.json [name ...]"""
import base64
import io
import json
import math
import os
import re
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
    if state.get('tsd'):
        svg = svg.replace('\n</svg>', '\n' + tsd_symbols(state['tsd']) + '\n</svg>')
    return svg


# The TSD's points are picture and text controls over the page (fza_mpd_fnc_uiDrawPoint), its route and sensor lines
# drawn on a canvas (fza_mpd_fnc_pageTSDDrawCanvas). Heading up: x right and y ahead of the aircraft, in metres.
TSD_LINE_COLOUR = '#00FF00'
TSD_LINE_WIDTH = 0.004
ICONS = os.path.join(paths.DOCS, 'assets', 'icons')


def ci_path(base, parts):
    """A path under base matched without regard to case, as the game's texture paths are."""
    for part in parts:
        names = {n.lower(): n for n in os.listdir(base)}
        base = os.path.join(base, names[part.lower()])
    return base


def tsd_sprite(tex):
    parts = tex.replace('\\', '/').strip('/').split('/')
    name = re.sub(r'(_ca)?\.paa$', '', parts[-1], flags=re.I) + '.png'
    low = [p.lower() for p in parts]
    if 'tsdicons' in low:
        return ci_path(os.path.join(ICONS, 'tsd'), parts[low.index('tsdicons') + 1:-1] + [name])
    return ci_path(os.path.join(ICONS, 'fcr'), [name])


def tinted_uri(path, rgba):
    from PIL import Image
    im = Image.open(path).convert('RGBA')
    r, g, b, a = im.split()
    bands = [band.point(lambda v, t=t: int(v * t)) for band, t in zip((r, g, b), rgba[:3])]
    buf = io.BytesIO()
    Image.merge('RGBA', bands + [a.point(lambda v: int(v * rgba[3]))]).save(buf, 'PNG')
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()


def tsd_symbols(spec):
    types = render.load_icon_types()

    def prop(name, key):
        c = types.get(name)
        while c is not None:
            v = c.get(key)
            if v is not None:
                return v
            c = types.get(c.base) if c.base else None
        return None

    s = 0.125 * 5 / spec.get('scale', 25000)
    cx, cy = 0.5, 0.75 - 0.25 * spec.get('ctr', 0)

    def screen(p):
        return cx + p[0] * s, cy - p[1] * s

    out = []
    for a, b in spec.get('lines', []):
        (x1, y1), (x2, y2) = screen(a), screen(b)
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
                   % (x1 * render.S, y1 * render.S, x2 * render.S, y2 * render.S, TSD_LINE_COLOUR, TSD_LINE_WIDTH * render.S))
    for p in spec.get('points', []):
        ident = p['ident'] if p['ident'] in types else 'Icon' + p['ident']
        size = prop(ident, 'size')
        colour = prop(ident, 'color')
        x, y = screen(p['at'])
        left, top = x - size / 2, y - size / 2
        for key in ('tex', 'tex2'):
            tex = prop(ident, key)
            if tex:
                out.append('<image x="%.1f" y="%.1f" width="%.1f" height="%.1f" href="%s"/>'
                           % (left * render.S, top * render.S, size * render.S, size * render.S, tinted_uri(tsd_sprite(tex), colour)))
        height = 0.00208 / size
        fill = '#%02X%02X%02X' % tuple(int(round(c * 255)) for c in colour[:3])
        for t in ('textA', 'textB'):
            text = prop(ident, t)
            if text is None or text == '':
                continue
            # fza_dms_fnc_pointFillIconText: 0 is the point's number, 1 its free text
            if not isinstance(text, str):
                text = '%02d' % p.get('id', 0) if int(text) == 0 else p.get('text', '')
            off = prop(ident, t + 'Offset') or [0, 0]
            h = (prop(ident, t + 'HAlign') or 'center').lower()
            v = (prop(ident, t + 'VAlign') or 'center').lower()
            ty = top + off[1] * size + {'top': height / 2, 'bottom': -height / 2}.get(v, 0)
            out.append('<text x="%.1f" y="%.1f" font-size="%.1f" fill="%s" text-anchor="%s" dominant-baseline="central">%s</text>'
                       % ((left + off[0] * size) * render.S, ty * render.S, height * render.S, fill,
                          {'left': 'start', 'right': 'end'}.get(h, 'middle'), render.esc(text)))
    return '\n'.join(out)


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
        '<!doctype html><html><head><style>@font-face{font-family:"BMKApacheFont";src:url("%s")}'
        'html,body{margin:0;background:#000}</style></head><body>%s</body></html>'
        % (paths.url(paths.FONT), open(svg_path, encoding='utf-8').read()))
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

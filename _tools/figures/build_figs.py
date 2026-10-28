"""Build every documentation figure listed in the docs repo's _data/figures/*.yml.

kind: mpd  -> native MPD page rendered from the preprocessed MFD config, in the cockpit model's bezel texture
kind: hud  -> IHADSS page rendered by its own JS in headless Chrome
Callout x/y may point anywhere inside the element; they are snapped to its edge facing the badge.
"""
import json
import os
import sys

import yaml
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fig  # noqa: E402
import paths  # noqa: E402
import render  # noqa: E402
import run  # noqa: E402

DOCS = paths.DOCS
OUT = paths.OUT
BEZEL_HREF = "{{ '/assets/figures/mpd-bezel.png' | relative_url }}"


def hud_png(model, out_png, transparent=False, weight=1):
    js = paths.mod('addons', 'fza_ah64_ihadss', 'ui', 'js')
    page = os.path.join(OUT, '_hud.html')
    scripts = ''.join('<script src="%s"></script>' % paths.url(os.path.join(js, f)) for f in
                      ['ihadss_common.js', 'ihadss_base.js', 'ihadss_flight.js', 'ihadss_weapon.js', 'ihadss_main.js'])
    open(page, 'w', encoding='utf-8').write(
        '<!doctype html><html><head><meta charset="utf-8"><style>@font-face{font-family:"BMKApacheFont";src:url("%s")}'
        'html,body{margin:0;padding:0;background:%s;overflow:hidden}#ihadss{display:block;width:1680px;height:1360px}</style></head>'
        '<body><canvas id="ihadss"></canvas>%s<script>window.IH.weight=%s;document.fonts.load("15px BMKApacheFont").then(function(){'
        'window.fzaIhadss.update(%s);});</script></body></html>'
        % (paths.url(paths.FONT), 'transparent' if transparent else '#000', scripts, weight, json.dumps(model)))
    paths.shoot([{'html': page, 'png': out_png, 'width': 1680, 'height': 1360, 'transparent': transparent, 'wait': 800}])


# The VIDEO page's symbology layer (fza_ah64_mpd/ui/video): the IHADSS canvas at 175vw x 141.67vw, left -37.5vw and
# top 50vh - 73.75vw on the square page, its lines and text 1.75 times as heavy
VIDEO_RECT = (-375.0, -237.5, 1750.0, 1416.667)
VIDEO_WEIGHT = 1.75


def video_layer(model):
    import base64
    png = os.path.join(OUT, '_video.png')
    hud_png(model, png, transparent=True, weight=VIDEO_WEIGHT)
    uri = 'data:image/png;base64,' + base64.b64encode(open(png, 'rb').read()).decode()
    return '<image x="%.1f" y="%.1f" width="%.1f" height="%.1f" href="%s"/>' % (VIDEO_RECT + (uri,))


def lit_fn(img, alpha=False):
    w, h = img.size
    px = img.load()

    def lit(x, y):
        x, y = int(round(x)), int(round(y))
        if x < 0 or y < 0 or x >= w or y >= h:
            return False
        p = px[x, y]
        return p[3] > 70 if alpha else (p[0] + p[1] + p[2]) > 150
    return lit


def build_mpd(fid, spec, mfd, consts, callouts, title):
    page = run.build(spec['state'], mfd, consts)
    if spec['state'].get('video'):
        page = page.replace('\n</svg>', '\n' + video_layer(spec['state']['video']) + '\n</svg>')
    svg_path = os.path.join(OUT, fid + '.svg')
    open(svg_path, 'w', encoding='utf-8').write(page)
    png = svg_path[:-4] + '.png'
    run.to_png(svg_path, png)
    fig.assign_sides(callouts, (0, 0, 1000, 1000))
    fig.snap(callouts, lit_fn(Image.open(png).convert('RGB')), lambda x, y: (x, y))
    lines, marks = fig.callout_layers(callouts, fig.MPD_BOX, 120) if callouts else ('', '')
    return fig.mpd_figure(page, callouts, fid, title, BEZEL_HREF, lines, marks)


HUD_SYMBOLS = os.path.join(paths.HERE, 'hud_symbols')
HUD_GREEN = (0x1A, 0xFF, 0x00)
# Format units each virtual symbol is drawn at (fza_ihadss_fnc_htmlIcons)
HUD_SYMBOL_SIZE = {'rkt': 128, 'rkt_inhibit': 128, 'rkt_stow': 128, 'rkt_stow_inhibit': 128}


def add_symbols(img, symbols):
    """The world-referenced symbols the game draws natively over the page: {sym, x, y, size?} in format units."""
    for s in symbols or []:
        name = s['sym']
        src = os.path.join(HUD_SYMBOLS, name + '.png') if '/' not in name else \
            os.path.join(DOCS, 'assets', 'icons', name + '.png')
        im = Image.open(src).convert('RGBA')
        px = int(2 * s.get('size', HUD_SYMBOL_SIZE.get(name, 30 if '/' in name else 64)))
        im = im.resize((px, px), Image.LANCZOS)
        r, g, b, a = im.split()
        lum = Image.merge('RGB', (r, g, b)).convert('L')
        tint = Image.merge('RGBA', [lum.point(lambda v, t=t: v * t // 255) for t in HUD_GREEN] + [a])
        x, y = int((s['x'] + 100) * 2 - px / 2), int((s['y'] + 100) * 2 - px / 2)
        img.alpha_composite(tint, (x, y))


def build_hud(fid, spec, callouts, title):
    png = os.path.join(DOCS, 'assets', 'figures', 'hud', fid + '.png')
    hud_png(spec['model'], png, transparent=True)
    img = Image.open(png).convert('RGBA')
    add_symbols(img, spec.get('symbols'))
    # crop: [x0, y0, x1, y1] in format units; the PNG is 2x with a 100 unit margin
    cx0, cy0, cx1, cy1 = spec.get('crop', [50, 20, 610, 490])
    img = img.crop(((cx0 + 100) * 2, (cy0 + 100) * 2, (cx1 + 100) * 2, (cy1 + 100) * 2))
    img.save(png, optimize=True)
    for c in callouts:
        c['x'] = (c['x'] - cx0) * 2
        c['y'] = (c['y'] - cy0) * 2
    w, h = img.size
    fig.assign_sides(callouts, (0, 0, w, h))
    fig.snap(callouts, lit_fn(img, alpha=True), lambda x, y: (x, y), gap=12, pad=8)
    lines, marks = fig.callout_layers(callouts, (0, 0, w, h), 80) if callouts else ('', '')
    return fig.hud_figure("{{ '/assets/figures/hud/%s.png' | relative_url }}" % fid, fid, title, lines, marks, callouts, (w, h))


def main(only):
    os.makedirs(OUT, exist_ok=True)
    mfd = consts = None
    figdir = os.path.join(DOCS, '_data', 'figures')
    for name in sorted(os.listdir(figdir)):
        fid = name[:-4]
        if not name.endswith('.yml') or (only and fid not in only):
            continue
        spec = yaml.safe_load(open(os.path.join(figdir, name), encoding='utf-8'))
        callouts = [dict(c) for c in spec.get('callouts') or []]
        title = spec.get('title', fid)
        kind = spec.get('kind', 'mpd')
        if kind == 'mpd':
            if mfd is None:
                mfd, consts = render.load_mfd(), render.load_constants()
            out = build_mpd(fid, spec, mfd, consts, callouts, title)
        elif kind == 'hud':
            out = build_hud(fid, spec, callouts, title)
        else:
            continue
        open(os.path.join(DOCS, '_includes', 'figures', fid + '.svg'), 'w', encoding='utf-8').write(out)
        print('figure', fid)


if __name__ == '__main__':
    main(set(sys.argv[1:]))

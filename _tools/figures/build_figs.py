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
# IHADSS crop, in format units: x 50..610, y 20..490 (the PNG is 2x)
HUD_CROP = (300, 240, 1420, 1180)


def hud_png(model, out_png, transparent=False):
    js = paths.mod('addons', 'fza_ah64_ihadss', 'ui', 'js')
    page = os.path.join(OUT, '_hud.html')
    scripts = ''.join('<script src="file://%s/%s"></script>' % (js, f) for f in
                      ['ihadss_common.js', 'ihadss_base.js', 'ihadss_flight.js', 'ihadss_weapon.js', 'ihadss_main.js'])
    open(page, 'w', encoding='utf-8').write(
        '<!doctype html><html><head><meta charset="utf-8"><style>@font-face{font-family:"BMKApacheFont";src:url("file://%s")}'
        'html,body{margin:0;padding:0;background:%s;overflow:hidden}#ihadss{display:block;width:1680px;height:1360px}</style></head>'
        '<body><canvas id="ihadss"></canvas>%s<script>document.fonts.load("15px BMKApacheFont").then(function(){'
        'window.fzaIhadss.update(%s);});</script></body></html>'
        % (paths.FONT, 'transparent' if transparent else '#000', scripts, json.dumps(model)))
    paths.shoot([{'html': page, 'png': out_png, 'width': 1680, 'height': 1360, 'transparent': transparent, 'wait': 800}])


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
    svg_path = os.path.join(OUT, fid + '.svg')
    open(svg_path, 'w', encoding='utf-8').write(page)
    png = svg_path[:-4] + '.png'
    run.to_png(svg_path, png)
    fig.assign_sides(callouts, (0, 0, 1000, 1000))
    fig.snap(callouts, lit_fn(Image.open(png).convert('RGB')), lambda x, y: (x, y))
    lines, marks = fig.callout_layers(callouts, fig.MPD_BOX, 120) if callouts else ('', '')
    return fig.mpd_figure(page, callouts, fid, title, BEZEL_HREF, lines, marks)


def build_hud(fid, spec, callouts, title):
    png = os.path.join(DOCS, 'assets', 'figures', 'hud', fid + '.png')
    hud_png(spec['model'], png, transparent=True)
    img = Image.open(png).convert('RGBA').crop(HUD_CROP)
    img.save(png, optimize=True)
    for c in callouts:
        c['x'] = (c['x'] - 50) * 2
        c['y'] = (c['y'] - 20) * 2
    fig.assign_sides(callouts, (0, 0, fig.HUD_W, fig.HUD_H))
    fig.snap(callouts, lit_fn(img, alpha=True), lambda x, y: (x, y), gap=12, pad=8)
    lines, marks = fig.callout_layers(callouts, (0, 0, fig.HUD_W, fig.HUD_H), 80) if callouts else ('', '')
    return fig.hud_figure("{{ '/assets/figures/hud/%s.png' | relative_url }}" % fid, fid, title, lines, marks, callouts)


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

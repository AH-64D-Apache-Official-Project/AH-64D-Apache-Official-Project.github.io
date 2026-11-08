"""Tint the FCR symbol sprites as the MPD shows them, for the manual's symbol tables and figures.

The sprites in assets/icons/fcr are white with dark detail; the game multiplies them by the MPD colour (yellow, the
shot-at marker green), keeping the dark detail. python icons.py writes assets/icons/fcr/mpd/<name>.png at 64 px.
"""
import base64
import io
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import paths  # noqa: E402

SRC = os.path.join(paths.DOCS, 'assets', 'icons', 'fcr')
OUT = os.path.join(SRC, 'mpd')
YELLOW = (255, 255, 0)
GREEN = (0, 255, 128)


def tinted(name, size=None):
    im = Image.open(os.path.join(SRC, name + '.png')).convert('RGBA')
    tint = GREEN if name == 'shotAT' else YELLOW
    r, g, b, a = im.split()
    bands = [band.point(lambda v, t=t: v * t // 255) for band, t in zip((r, g, b), tint)]
    out = Image.merge('RGBA', bands + [a])
    return out.resize((size, size), Image.LANCZOS) if size else out


def data_uri(name, alpha=1.0):
    im = tinted(name)
    if alpha < 1:
        im.putalpha(im.getchannel('A').point(lambda v: int(v * alpha)))
    buf = io.BytesIO()
    im.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('ascii')


TSD_SRC = os.path.join(paths.DOCS, 'assets', 'icons', 'tsd')
TSD_OUT = os.path.join(TSD_SRC, 'mpd')
# MPD_ICON_COLOR_* in fza_ah64_dms/headers/constants.h
ICON_COLOURS = {'GREEN': (0, 255, 128), 'BLUE': (102, 153, 255), 'RED': (255, 0, 51), 'YELLOW': (255, 255, 0)}
# Each ident's sprite and colour, from the mod's FzaIconTypes
TSD_IDENTS = {}
for _i in ['CC', 'LZ', 'PP', 'RP', 'SP', 'WP']:
    TSD_IDENTS[_i] = ('waypoints/' + _i, 'GREEN')
for _i in ['TO', 'TU', 'WL', 'WS']:
    TSD_IDENTS[_i] = ('hazards/' + _i, 'YELLOW')
for _i in ['AA', 'AG', 'AI', 'AL', 'AP', 'BP', 'BR', 'CP', 'FC', 'FF', 'FM', 'GL', 'HA']:
    TSD_IDENTS[_i] = ('controlMeasures/general/' + _i, 'GREEN')
TSD_IDENTS['ID'] = ('controlMeasures/general/ID', 'BLUE')
TSD_IDENTS['F1'] = TSD_IDENTS['F2'] = ('controlMeasures/general/F1_F2', 'RED')
for _i in ['AM', 'FI', 'FL', 'FU', 'MI']:
    TSD_IDENTS[_i] = ('controlMeasures/friendly/' + _i, 'BLUE')
for _i in ['AE', 'EF', 'EI', 'EM', 'EU']:
    TSD_IDENTS[_i] = ('controlMeasures/enemy/' + _i, 'RED')
for _i in [str(n) for n in range(1, 18)] + ['GU', 'S6', 'ZU', 'CT', 'CH', 'ST', 'HK', 'VU']:
    TSD_IDENTS[_i] = ('targetThreats/GU', 'RED')
TSD_IDENTS['SR'] = TSD_IDENTS['TR'] = ('targetThreats/R', 'RED')
TSD_IDENTS['TG'] = ('targetThreats/TG', 'RED')


def tsd_tinted(ident, size=64):
    src, colour = TSD_IDENTS[ident]
    im = Image.open(os.path.join(TSD_SRC, src + '.png')).convert('RGBA')
    r, g, b, a = im.split()
    bands = [band.point(lambda v, t=t: v * t // 255) for band, t in zip((r, g, b), ICON_COLOURS[colour])]
    return Image.merge('RGBA', bands + [a]).resize((size, size), Image.LANCZOS)


# The symbols for the manual's ident tables, with the text the TSD draws on them (fza_mpd_fnc_uiDrawPoint). Needs FM_MOD.
TSD_LABELLED = os.path.join(TSD_SRC, 'labelled')
LABEL_UNIT = 160         # pixels per icon width
LABEL_LEFT = 0.25        # canvas margins in icon widths, room for text outside the icon
LABEL_RIGHT = 0.55
LABEL_TOP = 0.2
LABEL_BOTTOM = 0.1
LABEL_FONT = 0.00208 / 0.09 / 0.09    # font height in icon widths: uiDrawPoint's 0.00208 / size, with ICON_SIZE 0.09
LABEL_FREE = 'AAA'       # sample free text
# Sample point numbers, valid for the point type (W01-W50, C51-C99, T01-T50) and in the order of the manual's ident tables
LABEL_NUMBER = {}
for _first, _idents in ((1, ['WP', 'SP', 'RP', 'PP', 'CC', 'LZ', 'TO', 'TU', 'WL', 'WS']),
                        (51, ['AP', 'AA', 'BP', 'BR', 'CP', 'FF', 'FM', 'FC', 'HA']),
                        (1, ['TG', 'SR', 'TR'])):
    for _n, _i in enumerate(_idents, _first):
        LABEL_NUMBER[_i] = '%02d' % _n


def icon_classes():
    """FzaIconTypes.hpp as {class: (base, {property: value})}."""
    text = open(paths.mod('addons', 'fza_ah64_mpd', 'FzaIconTypes.hpp'), encoding='utf-8').read()
    text = re.sub(r'//[^\n]*', '', text)
    classes = {}
    for m in re.finditer(r'class\s+(\w+)\s*(?::\s*(\w+)\s*)?\{', text):
        if m.group(1) == 'FzaIconTypes':
            continue
        depth, i = 1, m.end()
        while depth:
            depth += {'{': 1, '}': -1}.get(text[i], 0)
            i += 1
        props = {}
        for p in re.finditer(r'(\w+)(?:\[\])?\s*=\s*(\{[^}]*\}|"[^"]*"|[^;]+?)\s*;', text[m.end():i - 1]):
            props[p.group(1).lower()] = p.group(2).strip()
        classes[m.group(1)] = (m.group(2), props)
    return classes


def icon_prop(classes, name, key):
    while name:
        base, props = classes[name]
        if key.lower() in props:
            return props[key.lower()]
        name = base
    return None


def tsd_labelled(ident, classes):
    """The symbol on a canvas with room for its text, the text placed as the TSD places it."""
    name = ident if ident in classes else 'Icon' + ident
    unit = LABEL_UNIT
    width, height = int(unit * (LABEL_LEFT + 1 + LABEL_RIGHT)), int(unit * (LABEL_TOP + 1 + LABEL_BOTTOM))
    canvas = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    left, top = int(unit * LABEL_LEFT), int(unit * LABEL_TOP)
    canvas.alpha_composite(tsd_tinted(ident, unit), (left, top))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(paths.FONT, int(round(LABEL_FONT * unit)))
    em = LABEL_FONT * unit
    for t in ('textA', 'textB'):
        value = icon_prop(classes, name, t)
        if value is None:
            continue
        # fza_dms_fnc_pointFillIconText: MPD_ICON_TEXT_ID is the point's number, MPD_ICON_TEXT_FREE its free text
        if value == 'MPD_ICON_TEXT_ID':
            text = LABEL_NUMBER[ident]
        else:
            text = LABEL_FREE if value == 'MPD_ICON_TEXT_FREE' else value.strip('"')
        off = [float(v) for v in icon_prop(classes, name, t + 'Offset').strip('{}').split(',')]
        h = icon_prop(classes, name, t + 'HAlign').strip('"').lower()
        v = icon_prop(classes, name, t + 'VAlign').strip('"').lower()
        x = left + off[0] * unit
        y = top + off[1] * unit + {'top': em / 2, 'bottom': -em / 2}.get(v, 0)
        anchor = {'left': 'l', 'right': 'r'}.get(h, 'm') + 'm'
        box = draw.textbbox((x, y), text, font=font, anchor=anchor)
        if box[0] < 0 or box[1] < 0 or box[2] > width or box[3] > height:
            raise SystemExit('%s: text %r does not fit the canvas: %s' % (ident, text, box))
        draw.text((x, y), text, font=font, fill=ICON_COLOURS[TSD_IDENTS[ident][1]] + (255,), anchor=anchor)
    return canvas


if __name__ == '__main__':
    # python icons.py [fcr] [tsd] [labelled]: fcr and tsd by default
    sets = set(sys.argv[1:]) or {'fcr', 'tsd'}
    if 'labelled' in sets:
        os.makedirs(TSD_LABELLED, exist_ok=True)
        icon_types = icon_classes()
        for ident in TSD_IDENTS:
            tsd_labelled(ident, icon_types).save(os.path.join(TSD_LABELLED, ident + '.png'), optimize=True)
            print('labelled tsd icon', ident)
    if 'fcr' in sets:
        os.makedirs(OUT, exist_ok=True)
        for f in sorted(os.listdir(SRC)):
            if f.endswith('.png'):
                tinted(f[:-4], 64).save(os.path.join(OUT, f), optimize=True)
                print('icon', f)
    if 'tsd' in sets:
        os.makedirs(TSD_OUT, exist_ok=True)
        for ident in TSD_IDENTS:
            tsd_tinted(ident).save(os.path.join(TSD_OUT, ident + '.png'), optimize=True)
            print('tsd icon', ident)

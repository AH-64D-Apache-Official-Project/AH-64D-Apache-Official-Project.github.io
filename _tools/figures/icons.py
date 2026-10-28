"""Tint the FCR symbol sprites as the MPD shows them, for the manual's symbol tables and figures.

The sprites in assets/icons/fcr are white with dark detail; the game multiplies them by the MPD colour (yellow, the
shot-at marker green), keeping the dark detail. python icons.py writes assets/icons/fcr/mpd/<name>.png at 64 px.
"""
import base64
import io
import os
import sys

from PIL import Image

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


if __name__ == '__main__':
    # python icons.py [fcr] [tsd]: both sets by default
    sets = set(sys.argv[1:]) or {'fcr', 'tsd'}
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

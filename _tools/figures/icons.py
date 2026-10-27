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


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        if f.endswith('.png'):
            tinted(f[:-4], 64).save(os.path.join(OUT, f), optimize=True)
            print('icon', f)

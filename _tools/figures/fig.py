"""Compose documentation figures: an MPD bezel or IHADSS plate around a rendered page, with numbered reference lines.

Reference lines are drawn under the symbology and end on the edge of what they point at; only the end dot and the
numbered badge are drawn on top.
"""
import re

import bezel2

AMBER = '#ffb547'


def strip_svg(svg):
    """Inner content of a rendered page SVG, without its black backdrop."""
    inner = re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1)
    return inner.replace('<rect width="1000" height="1000" fill="#000"/>', '', 1)


def snap(callouts, lit, to_px, step=1.0, gap=10, pad=7):
    """Move each target from inside its element to the element's edge facing its badge.

    lit(px, py) -> bool on the raster; to_px(x, y) -> raster coords; step and pad are figure units, gap raster px."""
    for c in callouts:
        if c.get('snap') is False:
            continue
        dx, dy = {'l': (-1, 0), 'r': (1, 0), 't': (0, -1), 'b': (0, 1)}[c['_side']]
        x, y = float(c['x']), float(c['y'])
        last = None
        quiet = 0
        for i in range(2000):
            px, py = to_px(x, y)
            if lit(px, py):
                last = (x, y)
                quiet = 0
            else:
                quiet += 1
                if last is not None and quiet * step * abs(to_px(1, 1)[0] - to_px(0, 0)[0]) > gap:
                    break
                if last is None and i > 60:
                    break
            x += dx * step
            y += dy * step
        if last is not None:
            c['x'], c['y'] = last[0] + dx * pad, last[1] + dy * pad


def assign_sides(callouts, box):
    x0, y0, x1, y1 = box
    for c in callouts:
        s = c.get('side')
        if not s:
            d = {'l': c['x'] - x0, 'r': x1 - c['x'], 't': c['y'] - y0, 'b': y1 - c['y']}
            s = min(d, key=d.get)
        c['_side'] = s


def place(items, lo, hi, gap):
    """Spread badge positions along one gutter so they keep `gap` apart, staying near their targets."""
    items = sorted(items, key=lambda c: c['_t'])
    pos = [c['_t'] for c in items]
    for _ in range(300):
        moved = False
        for i in range(1, len(pos)):
            if pos[i] - pos[i - 1] < gap:
                d = (gap - (pos[i] - pos[i - 1])) / 2
                pos[i - 1] -= d
                pos[i] += d
                moved = True
        pos = [min(max(p, lo), hi) for p in pos]
        if not moved:
            break
    for c, p in zip(items, pos):
        c['_p'] = p


def callout_layers(callouts, box, gutter):
    """Returns (lines_svg, markers_svg)."""
    x0, y0, x1, y1 = box
    sides = {'l': [], 'r': [], 't': [], 'b': []}
    for c in callouts:
        c['_t'] = c['y'] if c['_side'] in 'lr' else c['x']
        sides[c['_side']].append(c)
    place(sides['l'], y0, y1, 58)
    place(sides['r'], y0, y1, 58)
    place(sides['t'], x0, x1, 64)
    place(sides['b'], x0, x1, 64)
    lines, marks = [], []
    for c in callouts:
        s, p, tx, ty = c['_side'], c['_p'], c['x'], c['y']
        stub = 34
        if s == 'l':
            bx, by = x0 - gutter, p
            pts = [(bx + 26, by), (tx - stub - 18, by), (tx - stub, ty), (tx, ty)]
        elif s == 'r':
            bx, by = x1 + gutter, p
            pts = [(bx - 26, by), (tx + stub + 18, by), (tx + stub, ty), (tx, ty)]
        elif s == 't':
            bx, by = p, y0 - gutter
            pts = [(bx, by + 26), (bx, ty - stub - 18), (tx, ty - stub), (tx, ty)]
        else:
            bx, by = p, y1 + gutter
            pts = [(bx, by - 26), (bx, ty + stub + 18), (tx, ty + stub), (tx, ty)]
        if (s in 'lr' and abs(by - ty) < 1) or (s in 'tb' and abs(bx - tx) < 1):
            pts = [pts[0], pts[-1]]
        d = 'M' + ' L'.join('%.1f %.1f' % q for q in pts)
        lines.append('<g class="co" data-n="%s"><path d="%s" fill="none" stroke="#000" stroke-opacity=".6" '
                     'stroke-width="8" stroke-linejoin="round"/><path class="co-line" d="%s" fill="none" stroke="%s" '
                     'stroke-width="3" stroke-linejoin="round"/></g>' % (c['n'], d, d, AMBER))
        marks.append('<g class="co" data-n="%s"><circle cx="%.1f" cy="%.1f" r="6.5" fill="%s" stroke="#000" stroke-width="2.5"/>'
                     '<circle cx="%.1f" cy="%.1f" r="25" fill="%s" stroke="#000" stroke-width="3"/>'
                     '<text x="%.1f" y="%.1f" fill="#111" font-family="IBM Plex Sans, sans-serif" font-weight="700" '
                     'font-size="26" text-anchor="middle">%s</text></g>'
                     % (c['n'], tx, ty, AMBER, bx, by, AMBER, bx, by + 9, c['n']))
    return '\n'.join(lines), '\n'.join(marks)


def svg_wrap(vb, title, body, font=True):
    return ('<svg class="fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" role="img" aria-label="%s"%s>\n'
            '%s\n</svg>\n' % (vb + (title, ' font-family="BMKApacheFont"' if font else '', body)))


MPD_BOX = (-245, -205, 1245, 1225)


def mpd_figure(page_svg, callouts, fig_id, title, texture_href, lines='', marks=''):
    pre = 'f%s-' % re.sub(r'\W', '', fig_id)
    tb = any(c.get('_side') == 't' for c in callouts)
    bb = any(c.get('_side') == 'b' for c in callouts)
    lr = any(c.get('_side') in 'lr' for c in callouts)
    x0 = -420 if lr else -265
    top = -380 if tb else -225
    bottom = 1395 if bb else 1245
    vb = (x0, top, -2 * x0 + 1000, bottom - top)
    body = [bezel2.bezel(pre, texture_href), lines, '<g>%s</g>' % strip_svg(page_svg), marks]
    return svg_wrap(vb, title, '\n'.join(body))


HUD_W, HUD_H = 1120, 940


def hud_figure(href, fig_id, title, lines='', marks='', callouts=()):
    tb = any(c.get('_side') == 't' for c in callouts)
    bb = any(c.get('_side') == 'b' for c in callouts)
    top = -50 - (100 if tb else 0)
    bottom = HUD_H + 50 + (100 if bb else 0)
    vb = (-140, top, HUD_W + 280, bottom - top)
    body = ['<rect x="0" y="0" width="%d" height="%d" rx="18" fill="#030503"/>' % (HUD_W, HUD_H), lines,
            '<image href="%s" x="0" y="0" width="%d" height="%d"/>' % (href, HUD_W, HUD_H), marks]
    return svg_wrap(vb, title, '\n'.join(body), font=False)

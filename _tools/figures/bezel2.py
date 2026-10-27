"""MPD bezel candidates built on the cockpit model's MPD texture (fza_ah64_model/tex/In/MPD_co.paa).

Display units: the page is 1000x1000. The texture's VAB ticks sit 40 px apart, which puts the screen at texture
(86.5, 79.3) with 333.3 px per page width, so one texture px = 3 units.
"""
TX0, TY0, K = 86.5, 79.3, 3.0


def u(tx, ty):
    return (tx - TX0) * K, (ty - TY0) * K


TB = [157 + 40 * i for i in range(6)]
LR = [145 + 40 * i for i in range(6)]
ROW_T, ROW_B, COL_L, COL_R = 43, 458, 47, 465


def caps():
    """[(x, y, w, h, label, id)] in units."""
    out = []
    for i, tx in enumerate(TB):
        x, y = u(tx, ROW_T)
        out.append((x, y, 58, 50, '', 'T%d' % (i + 1)))
        x, y = u(tx, ROW_B)
        out.append((x, y, 58, 50, 'M' if i == 0 else '', 'B%d' % (i + 1)))
    for i, ty in enumerate(LR):
        x, y = u(COL_L, ty)
        out.append((x, y, 58, 52, '', 'L%d' % (i + 1)))
        x, y = u(COL_R, ty)
        out.append((x, y, 58, 52, '', 'R%d' % (i + 1)))
    for name, tx, ty in [('FCR', COL_L, 384), ('WPN', COL_L, 424), ('COM', COL_R, 384), ('VID', COL_R, 424),
                         ('TSD', 107, ROW_B), ('A/C', 399, ROW_B)]:
        x, y = u(tx, ty)
        out.append((x, y, 64, 52, name, ''))
    return out


def defs(p):
    return ('<defs><linearGradient id="%scap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b706c"/>'
            '<stop offset=".5" stop-color="#4a4f4b"/><stop offset="1" stop-color="#2f3330"/></linearGradient>'
            '<radialGradient id="%sglass" cx=".35" cy=".25" r="1"><stop offset="0" stop-color="#0b120b"/>'
            '<stop offset="1" stop-color="#020302"/></radialGradient>'
            '<clipPath id="%sclip"><rect x="-245" y="-205" width="1490" height="1430" rx="40"/></clipPath></defs>') % (p, p, p)


def bezel(p, texture_href, ids=True, tone=''):
    o = [defs(p)]
    x0, y0 = u(0, 0)
    o.append('<g clip-path="url(#%sclip)"><image href="%s" x="%.1f" y="%.1f" width="1536" height="1536" %s/></g>'
             % (p, texture_href, x0, y0, tone))
    o.append('<rect x="-245" y="-205" width="1490" height="1430" rx="40" fill="none" stroke="#000" stroke-opacity=".6" stroke-width="4"/>')
    # screen recess and glass
    o.append('<rect x="-22" y="-22" width="1044" height="1060" rx="12" fill="#151716" stroke="#0a0b0a" stroke-width="3"/>')
    o.append('<rect x="-8" y="-8" width="1016" height="1016" rx="6" fill="url(#%sglass)"/>' % p)
    lab = 'font-family="IBM Plex Sans, sans-serif" font-weight="600" text-anchor="middle"'
    for x, y, w, h, name, cid in caps():
        o.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="8" fill="url(#%scap)" stroke="#121413" stroke-width="3"/>'
                 % (x - w / 2, y - h / 2, w, h, p))
        o.append('<rect x="%.1f" y="%.1f" width="%d" height="3" rx="1.5" fill="#fff" fill-opacity=".18"/>'
                 % (x - w / 2 + 6, y - h / 2 + 4, w - 12))
        if name:
            o.append('<text x="%.1f" y="%.1f" fill="#eef1ee" font-size="%d" %s>%s</text>'
                     % (x, y + 7, 21 if len(name) < 3 else 18, lab, name))
        if ids and cid:
            if cid[0] == 'T':
                tx, ty = x, y - h / 2 - 12
            elif cid[0] == 'B':
                tx, ty = x, y + h / 2 + 30
            elif cid[0] == 'L':
                tx, ty = x - w / 2 - 34, y + 8
            else:
                tx, ty = x + w / 2 + 34, y + 8
            o.append('<text x="%.1f" y="%.1f" fill="#9aa39c" font-size="22" %s>%s</text>' % (tx, ty, lab, cid))
    return '\n'.join(o)


VIEW = (-330, -290, 1660, 1610)

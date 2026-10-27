"""Render an Arma MFD config class (preprocessed, parsed by cfg.py) to SVG for a given state."""
import math
import os
import pickle
import re
import sys

sys.setrecursionlimit(10000)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cfg  # noqa: E402
import paths  # noqa: E402

S = 1000.0
MPD_OFFSET_L = 20


def load_mfd():
    cache = os.path.join(paths.CACHE, 'mfd.pickle')
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    pre = os.path.join(paths.CACHE, 'mpd_pre.cpp')
    if not os.path.exists(pre):
        import prep
        prep.run('fza_ah64_mpd/config.cpp', pre)
    root = cfg.load(pre)
    mfd = cfg.find(root, ['CfgVehicles', 'fza_ah64base', 'MFD', 'MPD_L'])
    pickle.dump(mfd, open(cache, 'wb'))
    return mfd


def load_mags():
    """CfgMagazines from the MPD addon: the pylon icons (mfdElements) the WPN page draws on each station."""
    cache = os.path.join(paths.CACHE, 'mags.pickle')
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    pre = os.path.join(paths.CACHE, 'mpd_pre.cpp')
    if not os.path.exists(pre):
        import prep
        prep.run('fza_ah64_mpd/config.cpp', pre)
    text = open(pre, encoding='utf-8').read()
    start = text.index('class CfgMagazines')
    depth, i = 0, text.index('{', start)
    while True:
        depth += {'{': 1, '}': -1}.get(text[i], 0)
        if depth == 0:
            break
        i += 1
    # the icons' text macros name MFD_OFFSET, which is only defined inside the MPD classes
    block = re.sub(r'\bMFD_OFFSET\b', str(MPD_OFFSET_L), text[start:i + 1])
    mags = cfg.find(cfg.parse(block + ';'), ['CfgMagazines'])
    pickle.dump(mags, open(cache, 'wb'))
    return mags


def load_constants():
    consts = {}
    for line in open(paths.mod('addons', 'fza_ah64_mpd', 'headers', 'mfdConstants.h'), encoding='utf-8'):
        m = re.match(r'\s*#define\s+(\w+)\s+(.+?)\s*(//.*)?$', line)
        if not m:
            continue
        expr = m.group(2)
        for k in sorted(consts, key=len, reverse=True):
            expr = re.sub(r'\b%s\b' % k, str(consts[k]), expr)
        try:
            consts[m.group(1)] = int(cfg.STATIC.eval(expr))
        except Exception:
            pass
    return consts


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Renderer:
    def __init__(self, mfd, user=None, text=None, sources=None, page_offset=MPD_OFFSET_L, pylons=None, mags=None):
        self.mfd = mfd
        # pylons: {pylon number: magazine class from the MPD addon's CfgMagazines}
        self.pylons = {int(k): v for k, v in (pylons or {}).items()}
        self.mags = mags
        self.offset = (0.0, 0.0)
        self.user = {}
        self.text = {}
        self.vars = {'heading': 0.0, 'altitudeAGL': 0.0, 'horizonBank': 0.0, 'horizonDive': 0.0, 'speed': 0.0}
        self.vars.update(sources or {})
        for k, v in (user or {}).items():
            self.user[k] = v
        for k, v in (text or {}).items():
            self.text[k] = v
        self.bones = {b.name.lower(): b for b in mfd.child('Bones').classes()}
        for b in list(self.bones.values()):
            seen, base = set(), b.base
            while base and base.lower() in self.bones and base.lower() not in seen:
                seen.add(base.lower())
                parent = self.bones[base.lower()]
                have = {i[1].lower() for i in b.items if i[0] == 'prop'}
                b.items = b.items + [i for i in parent.items if i[0] == 'prop' and i[1].lower() not in have]
                base = parent.base
        self.out = []
        self.clip_id = 0
        self.defs = []

    # -- expressions
    def ev(self, v):
        if isinstance(v, (int, float, bool)):
            return float(v)
        if isinstance(v, str):
            vars_ = dict(self.vars)
            for k, val in self.user.items():
                vars_['user%d' % k] = float(val)
            try:
                return cfg.num(cfg.Evaluator(vars_).eval(v))
            except cfg.SqfError as e:
                sys.stderr.write('expr fail %r: %s\n' % (v, e))
                return 0.0
        return 0.0

    def src(self, name, index=0):
        if name == 'user':
            return float(self.user.get(int(index), 0.0))
        return float(self.vars.get(name, 0.0))

    # -- bones
    def bone(self, name, off):
        b = self.bones.get(name.lower())
        x, y = off
        if b is None:
            return x, y
        t = (b.get('type') or '').lower()
        if t == 'fixed':
            p = b.get('pos', [0, 0])
            return p[0] + x, p[1] + y
        if t == 'linear':
            v = self.src(b.get('source', ''), b.get('sourceIndex', 0)) * float(b.get('sourceScale', 1))
            lo, hi = float(b.get('min', 0)), float(b.get('max', 1))
            f = 0.0 if hi == lo else max(0.0, min(1.0, (v - lo) / (hi - lo)))
            # the game moves a linear bone from maxPos at min to minPos at max
            a, c = b.get('maxPos', [0, 0]), b.get('minPos', [0, 0])
            return a[0] + (c[0] - a[0]) * f + x, a[1] + (c[1] - a[1]) * f + y
        if t == 'rotational':
            v = self.src(b.get('source', ''), b.get('sourceIndex', 0)) * float(b.get('sourceScale', 1))
            lo, hi = float(b.get('min', 0)), float(b.get('max', 1))
            f = 0.0 if hi == lo else max(0.0, min(1.0, (v - lo) / (hi - lo)))
            # like linear bones, the game takes maxAngle at min and minAngle at max
            ang = math.radians(float(b.get('maxAngle', 0)) + (float(b.get('minAngle', 0)) - float(b.get('maxAngle', 0))) * f)
            cx, cy = b.get('center', [0.5, 0.5])
            ar = float(b.get('aspectRatio', 1))
            # positive angles turn anticlockwise on the display
            rx = x * math.cos(ang) + y * ar * math.sin(ang)
            ry = (-x * math.sin(ang) + y * ar * math.cos(ang)) / ar
            return cx + rx, cy + ry
        if t == 'horizon':
            # offsets are screen units about pos0; pitch moves the horizon (pos10 - pos0) per 10 deg
            p0 = b.get('pos0', [0.5, 0.5])
            p10 = b.get('pos10', [0.6, 0.6])
            pitch = float(self.vars.get('pitch', 0.0))
            bank = math.radians(float(self.vars.get('bank', 0.0)))
            py = y + pitch * (p10[1] - p0[1]) / 10.0
            c, sn = math.cos(-bank), math.sin(-bank)
            return p0[0] + x * c - py * sn, p0[1] + x * sn + py * c
        return x, y

    def point(self, p):
        """Resolve a point entry to (x, y), or None for a break."""
        if not p:
            return None
        if isinstance(p[0], list):
            w = self.ev(p[1]) if len(p) > 1 else 1.0
            return p[0][0] * w + self.offset[0], p[0][1] * w + self.offset[1]
        x = y = 0.0
        i = 0
        while i < len(p):
            if isinstance(p[i], list):
                w = self.ev(p[i + 1]) if i + 1 < len(p) else 1.0
                x += p[i][0] * w
                y += p[i][1] * w
                i += 2
                continue
            name = str(p[i]).strip()
            if i + 1 < len(p) and isinstance(p[i + 1], list):
                off = p[i + 1]
                w = self.ev(p[i + 2]) if i + 2 < len(p) else 1.0
                i += 3
            else:
                off = [0.0, 0.0]
                w = self.ev(p[i + 1]) if i + 1 < len(p) else 1.0
                i += 2
            bx, by = self.bone(name, off)
            x += bx * w
            y += by * w
        return x + self.offset[0], y + self.offset[1]

    # -- drawing
    def resolve(self, node, parent, parent_base):
        """Merge a draw class with the class it inherits from: a sibling (class Ready: Deselected),
        or the same-named class in the parent's base (class Pylon: Pylon)."""
        if not node.base:
            return node, None
        cand = None
        if node.base.lower() != node.name.lower() and parent is not None:
            cand = parent.child(node.base)
        if cand is None and parent_base is not None:
            cand = parent_base.child(node.base)
        if cand is None or cand is node:
            return node, None
        cand, _ = self.resolve(cand, parent, None)
        have_p = {i[1].lower() for i in node.items if i[0] == 'prop'}
        have_c = {i[1].name.lower() for i in node.items if i[0] == 'class'}
        merged = cfg.Node(node.name)
        merged.items = [i for i in cand.items if (i[0] == 'prop' and i[1].lower() not in have_p)
                        or (i[0] == 'class' and i[1].name.lower() not in have_c)] + node.items
        return merged, cand

    def draw(self, node, color, width_scale=1.0, parent=None, parent_base=None):
        node, base = self.resolve(node, parent, parent_base)
        cond = node.get('condition')
        if cond is not None and self.ev(cond) <= 0:
            return
        col = node.get('color')
        if isinstance(col, list) and len(col) >= 3:
            color = [self.ev(c) for c in col] + ([1.0] if len(col) == 3 else [])
        if len(color) > 3 and color[3] <= 0.01:
            return
        clip_open = False
        tl, br = node.get('clipTL'), node.get('clipBR')
        if tl and br:
            self.clip_id += 1
            cid = 'c%d' % self.clip_id
            self.defs.append('<clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f"/></clipPath>'
                             % (cid, tl[0] * S, tl[1] * S, (br[0] - tl[0]) * S, (br[1] - tl[1]) * S))
            self.out.append('<g clip-path="url(#%s)">' % cid)
            clip_open = True
        t = (node.get('type') or '').lower()
        if t == 'line':
            self.line(node, color)
        elif t == 'polygon':
            self.polygon(node, color)
        elif t == 'text':
            self.text_el(node, color)
        elif t == 'pylonicon':
            self.pylon(node, color)
        for c in node.classes():
            self.draw(c, color, parent=node, parent_base=base)
        if clip_open:
            self.out.append('</g>')

    def rgba(self, c):
        r, g, b = (max(0, min(255, int(round(v * 255)))) for v in c[:3])
        a = c[3] if len(c) > 3 else 1
        return '#%02x%02x%02x' % (r, g, b), a

    def line(self, node, color):
        pts = node.get('points') or []
        w = float(self.ev(node.get('width', 1)))
        rgb, a = self.rgba(color)
        segs, cur = [], []
        for p in pts:
            q = self.point(p)
            if q is None:
                if len(cur) > 1:
                    segs.append(cur)
                cur = []
            else:
                cur.append(q)
        if len(cur) > 1:
            segs.append(cur)
        for seg in segs:
            d = 'M' + ' L'.join('%.2f %.2f' % (x * S, y * S) for x, y in seg)
            lt = int(self.ev(node.get('lineType', 0)))
            dash = {1: ' stroke-dasharray="2 9"', 2: ' stroke-dasharray="14 10"', 3: ' stroke-dasharray="14 8 3 8"'}.get(lt, '')
            self.out.append('<path d="%s" fill="none" stroke="%s" stroke-opacity="%.2f" stroke-width="%.2f" '
                            'stroke-linecap="round" stroke-linejoin="round"%s/>' % (d, rgb, a, max(1.0, w * 1.15), dash))

    def polygon(self, node, color):
        rgb, a = self.rgba(color)
        for poly in node.get('points') or []:
            pts = [self.point(p) for p in poly if p]
            pts = [p for p in pts if p]
            if len(pts) < 3:
                continue
            d = 'M' + ' L'.join('%.2f %.2f' % (x * S, y * S) for x, y in pts) + ' Z'
            self.out.append('<path d="%s" fill="%s" fill-opacity="%.2f"/>' % (d, rgb, a))

    def text_value(self, node):
        source = (node.get('source') or 'static').lower()
        if source == 'static':
            t = node.get('text', '')
            # a number in the config reads like the game prints it: text = 1 shows "1"
            t = ('%d' % t) if isinstance(t, float) and t == int(t) else str(t)
            if 'Â' in t or 'Ã' in t:
                try:
                    t = t.encode('latin1').decode('utf8')
                except UnicodeError:
                    pass
            return t
        if source == 'usertext':
            return str(self.text.get(int(node.get('sourceIndex', 0)), ''))
        v = self.src(node.get('source'), node.get('sourceIndex', 0)) * float(node.get('sourceScale', 1))
        prec = int(node.get('sourcePrecision', 0))
        return ('%.' + str(prec) + 'f') % v

    def text_el(self, node, color):
        s = self.text_value(node)
        if not s:
            return
        pos = self.point(node.get('pos'))
        right = self.point(node.get('right'))
        down = self.point(node.get('down'))
        if not pos or not right or not down:
            return
        scale = float(self.ev(node.get('scale', 1)))
        cw = math.hypot(right[0] - pos[0], right[1] - pos[1]) * scale
        ch = math.hypot(down[0] - pos[0], down[1] - pos[1]) * scale
        adv = cw * 0.0205 / 0.025
        n = len(s)
        width = adv * n
        align = (node.get('align') or 'left').lower()
        x0 = pos[0]
        # Arma's align names the side of the anchor the text grows towards
        if align == 'center':
            x0 -= width / 2
        elif align == 'left':
            x0 -= width
        fs = ch * 1000.0 / 924.0
        base = pos[1] + fs * 0.754
        rgb, a = self.rgba(color)
        self.out.append('<text xml:space="preserve" x="%.2f" y="%.2f" font-size="%.2f" textLength="%.2f" lengthAdjust="spacingAndGlyphs" '
                        'fill="%s" fill-opacity="%.2f">%s</text>'
                        % (x0 * S, base * S, fs * S, width * S, rgb, a, esc(s)))

    def pylon(self, node, color):
        mag = self.pylons.get(int(self.ev(node.get('pylon', 0))))
        if not mag or self.mags is None:
            return
        elems = self.mags.child(mag)
        elems = elems.child('mfdElements') if elems is not None else None
        icon = elems.child(str(node.get('name'))) if elems is not None else None
        draw = icon.child('Draw') if icon is not None else None
        if draw is None:
            return
        pos = self.point(node.get('pos'))
        saved = self.offset, self.vars.get('pylonMagazineEmpty')
        self.offset = pos
        self.vars['pylonMagazineEmpty'] = 0.0
        for c in draw.classes():
            self.draw(c, color)
        self.offset = saved[0]
        self.vars['pylonMagazineEmpty'] = saved[1] or 0.0

    def render(self, page, size=1000):
        draw = self.mfd.child('Draw')
        base = self.mfd.get('color', [0.2, 1, 0, 1])
        self.user.setdefault(1, page)
        for c in draw.classes():
            self.draw(c, list(base))
        body = '\n'.join(self.out)
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
                'font-family="BMKApacheFont">\n<defs>%s</defs>\n<rect width="%d" height="%d" fill="#000"/>\n%s\n</svg>'
                % (S, S, size, size, ''.join(self.defs), S, S, body))

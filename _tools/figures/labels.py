"""List the text drawn next to each VAB for page states: python labels.py states.json name [name...]"""
import json
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render  # noqa: E402
import run  # noqa: E402

TB = [0.21, 0.33, 0.45, 0.57, 0.69, 0.81]
LR = [0.2, 0.315, 0.43, 0.545, 0.66, 0.775]


def vab(x, y):
    if y < 0.09:
        return 'T%d' % (min(range(6), key=lambda i: abs(TB[i] - x)) + 1)
    if y > 0.9:
        return 'B%d' % (min(range(6), key=lambda i: abs(TB[i] - x)) + 1)
    if x < 0.16:
        return 'L%d' % (min(range(6), key=lambda i: abs(LR[i] - y)) + 1)
    if x > 0.84:
        return 'R%d' % (min(range(6), key=lambda i: abs(LR[i] - y)) + 1)
    return None


class Cap(render.Renderer):
    def text_el(self, node, color):
        s = self.text_value(node)
        pos = self.point(node.get('pos'))
        if s and pos:
            self.caps.append((vab(pos[0], pos[1]), round(pos[0], 3), round(pos[1], 3), s))


def labels(state, mfd, consts):
    off = render.MPD_OFFSET_L
    user, text = {}, {}
    for k, v in state.get('u', {}).items():
        user[(consts[k] if not k.isdigit() else int(k)) + off] = v
    for k, v in state.get('t', {}).items():
        text[(consts[k] if not k.isdigit() else int(k)) + off] = v
    for k, v in state.get('raw', {}).items():
        user[int(k)] = v
    r = Cap(mfd, user, text, state.get('src'))
    r.caps = []
    r.render(consts['MPD_PAGE_' + state['page']])
    return r.caps


if __name__ == '__main__':
    mfd, consts = render.load_mfd(), render.load_constants()
    states = json.load(open(sys.argv[1], encoding='utf-8'))
    for name in sys.argv[2:]:
        caps = labels(states[name], mfd, consts)
        by = {}
        rest = []
        for b, x, y, s in caps:
            if b:
                by.setdefault(b, []).append(s)
            else:
                rest.append('%s@(%.2f,%.2f)' % (s, x, y))
        order = ['T%d' % i for i in range(1, 7)] + ['L%d' % i for i in range(1, 7)] + ['R%d' % i for i in range(1, 7)] + ['B%d' % i for i in range(1, 7)]
        print('==', name)
        print('  ' + ' | '.join('%s: %s' % (b, ' / '.join(by[b])) for b in order if b in by))
        print('  other: ' + ', '.join(rest[:80]))

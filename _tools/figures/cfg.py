"""Arma config parser and SQF-subset evaluator for preprocessed MFD configs."""
import math
import re


# ---------------------------------------------------------------- SQF subset

class SqfError(Exception):
    pass


TOKEN_RE = re.compile(r'''
    (?P<ws>\s+)
  | (?P<num>(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)
  | (?P<str>"(?:[^"]|"")*"|'(?:[^']|'')*')
  | (?P<op>\|\||&&|==|!=|>=|<=|[-+*/%^<>!()\[\],])
  | (?P<id>[A-Za-z_][A-Za-z_0-9]*)
''', re.X)


def tokenize(s):
    out, i = [], 0
    while i < len(s):
        m = TOKEN_RE.match(s, i)
        if not m:
            raise SqfError('bad char %r in %r' % (s[i], s))
        i = m.end()
        k = m.lastgroup
        if k == 'ws':
            continue
        v = m.group(k)
        if k == 'num':
            out.append(('num', float(v)))
        elif k == 'str':
            q = v[0]
            out.append(('str', v[1:-1].replace(q + q, q)))
        elif k == 'id':
            out.append(('id', v))
        else:
            out.append(('op', v))
    out.append(('end', None))
    return out


BINARY = {
    '||': 1, 'or': 1, '&&': 2, 'and': 2,
    '==': 3, '!=': 3, '<': 3, '>': 3, '<=': 3, '>=': 3,
    'select': 4, 'factor': 4, 'interpolate': 4,
    '+': 5, '-': 5, 'min': 5, 'max': 5,
    '*': 6, '/': 6, '%': 6, 'mod': 6, 'atan2': 6,
    '^': 7,
}
UNARY = {'-', '+', '!', 'not', 'floor', 'ceil', 'round', 'abs', 'str', 'format', 'cos', 'sin', 'tan',
         'sqrt', 'count', 'toupper', 'tolower', 'deg', 'rad', 'acos', 'asin', 'atan'}


def num(v):
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, (int, float)):
        return float(v)
    raise SqfError('not a number: %r' % (v,))


def sqf_str(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, float):
        if v == int(v) and abs(v) < 1e15:
            return str(int(v))
        return ('%.6g' % v)
    if isinstance(v, list):
        return '[' + ','.join(sqf_str(x) if not isinstance(x, str) else '"%s"' % x for x in v) + ']'
    return str(v)


def sqf_format(args):
    fmt = args[0]
    def rep(m):
        i = int(m.group(1))
        return sqf_str(args[i]) if i < len(args) else ''
    return re.sub(r'%(\d+)', rep, fmt)


class Evaluator:
    def __init__(self, variables=None):
        self.vars = variables if variables is not None else {}

    def eval(self, src):
        self.toks = tokenize(src)
        self.i = 0
        v = self.expr(0)
        if self.toks[self.i][0] != 'end':
            raise SqfError('trailing tokens in %r at %r' % (src, self.toks[self.i:]))
        return v

    def peek(self):
        return self.toks[self.i]

    def take(self):
        t = self.toks[self.i]
        self.i += 1
        return t

    def expr(self, minprec):
        left = self.unary()
        while True:
            k, v = self.peek()
            op = v.lower() if k == 'id' else v
            if k not in ('op', 'id') or op not in BINARY or BINARY[op] <= minprec - 1 or BINARY[op] < minprec:
                return left
            prec = BINARY[op]
            self.take()
            right = self.expr(prec + 1)
            left = self.binary(op, left, right)

    def binary(self, op, a, b):
        if op in ('||', 'or'):
            return bool(num(a)) or bool(num(b))
        if op in ('&&', 'and'):
            return bool(num(a)) and bool(num(b))
        if op == '==':
            return a == b if isinstance(a, str) else num(a) == num(b)
        if op == '!=':
            return a != b if isinstance(a, str) else num(a) != num(b)
        if op in ('<', '>', '<=', '>='):
            a, b = num(a), num(b)
            return {'<': a < b, '>': a > b, '<=': a <= b, '>=': a >= b}[op]
        if op == 'select':
            if isinstance(b, bool):
                return a[1] if b else a[0]
            return a[int(round(num(b)))]
        if op == 'factor':
            lo, hi = num(b[0]), num(b[1])
            x = num(a)
            if hi == lo:
                return 0.0
            return max(0.0, min(1.0, (x - lo) / (hi - lo)))
        if op == 'interpolate':
            lo, hi, v0, v1 = (num(x) for x in b)
            t = 0.0 if hi == lo else max(0.0, min(1.0, (num(a) - lo) / (hi - lo)))
            return v0 + (v1 - v0) * t
        if op == '+':
            if isinstance(a, str) or isinstance(b, str):
                return str(a) + str(b)
            if isinstance(a, list):
                return a + b
            return num(a) + num(b)
        if op == '-':
            return num(a) - num(b)
        if op == 'min':
            return min(num(a), num(b))
        if op == 'max':
            return max(num(a), num(b))
        if op == '*':
            return num(a) * num(b)
        if op == '/':
            b = num(b)
            return num(a) / b if b else 0.0
        if op in ('%', 'mod'):
            b = num(b)
            return math.fmod(num(a), b) if b else 0.0
        if op == 'atan2':
            return math.degrees(math.atan2(num(a), num(b)))
        if op == '^':
            return num(a) ** num(b)
        raise SqfError(op)

    def unary(self):
        k, v = self.peek()
        op = v.lower() if k == 'id' else v
        if (k == 'op' and v in ('-', '+', '!')) or (k == 'id' and op in UNARY):
            self.take()
            x = self.unary()
            if op == '-':
                return -num(x)
            if op == '+':
                return num(x)
            if op in ('!', 'not'):
                return not bool(num(x))
            if op == 'floor':
                return float(math.floor(num(x)))
            if op == 'ceil':
                return float(math.ceil(num(x)))
            if op == 'round':
                return float(math.floor(num(x) + 0.5))
            if op == 'abs':
                return abs(num(x))
            if op == 'str':
                return sqf_str(x)
            if op == 'format':
                return sqf_format(x)
            if op in ('cos', 'sin', 'tan'):
                return getattr(math, op)(math.radians(num(x)))
            if op in ('acos', 'asin', 'atan'):
                return math.degrees(getattr(math, op)(num(x)))
            if op == 'sqrt':
                return math.sqrt(num(x))
            if op == 'count':
                return float(len(x))
            if op == 'toupper':
                return x.upper()
            if op == 'tolower':
                return x.lower()
            if op == 'deg':
                return math.degrees(num(x))
            if op == 'rad':
                return math.radians(num(x))
        return self.primary()

    def primary(self):
        k, v = self.take()
        if k == 'num' or k == 'str':
            return v
        if k == 'op' and v == '(':
            x = self.expr(0)
            self.expect(')')
            return x
        if k == 'op' and v == '[':
            items = []
            if self.peek() != ('op', ']'):
                while True:
                    items.append(self.expr(0))
                    if self.peek() == ('op', ','):
                        self.take()
                        continue
                    break
            self.expect(']')
            return items
        if k == 'id':
            lv = v.lower()
            if lv == 'true':
                return True
            if lv == 'false':
                return False
            if v in self.vars:
                return self.vars[v]
            if lv in self.vars:
                return self.vars[lv]
            m = re.fullmatch(r'user(\d+)', v)
            if m:
                return 0.0
            raise SqfError('unknown variable %r' % v)
        raise SqfError('unexpected %r %r' % (k, v))

    def expect(self, v):
        t = self.take()
        if t != ('op', v):
            raise SqfError('expected %r got %r' % (v, t))


STATIC = Evaluator()


def eval_static(raw):
    """Evaluate a config scalar: __EVAL() blocks, string literals and arithmetic."""
    raw = raw.strip()
    if '__EVAL' in raw:
        out, i = [], 0
        while True:
            j = raw.find('__EVAL(', i)
            if j < 0:
                out.append(raw[i:])
                break
            out.append(raw[i:j])
            k, depth, instr = j + 7, 1, None
            while depth:
                c = raw[k]
                if instr:
                    if c == instr:
                        instr = None
                elif c in '"\'':
                    instr = c
                elif c in '([{':
                    depth += 1
                elif c in ')]}':
                    depth -= 1
                k += 1
            try:
                val = STATIC.eval(raw[j + 7:k - 1])
            except SqfError:
                return raw
            out.append('"%s"' % val.replace('"', '""') if isinstance(val, str) else sqf_str(val))
            i = k
        raw = ''.join(out)
    try:
        return STATIC.eval(raw)
    except SqfError:
        return raw


# ---------------------------------------------------------------- config parser

class Node:
    __slots__ = ('name', 'base', 'items')

    def __init__(self, name, base=None):
        self.name = name
        self.base = base
        self.items = []  # ('prop', name, value) or ('class', Node)

    def props(self):
        return {n: v for k, n, v in (i for i in self.items if i[0] == 'prop')}

    def get(self, key, default=None):
        for it in self.items:
            if it[0] == 'prop' and it[1].lower() == key.lower():
                return it[2]
        return default

    def classes(self):
        return [i[1] for i in self.items if i[0] == 'class']

    def child(self, name):
        for c in self.classes():
            if c.name.lower() == name.lower():
                return c
        return None


class Parser:
    def __init__(self, text):
        self.s = text
        self.i = 0
        self.n = len(text)

    def ws(self):
        s, n = self.s, self.n
        while self.i < n:
            c = s[self.i]
            if c.isspace():
                self.i += 1
            elif s.startswith('//', self.i):
                j = s.find('\n', self.i)
                self.i = n if j < 0 else j
            elif s.startswith('/*', self.i):
                j = s.find('*/', self.i)
                self.i = n if j < 0 else j + 2
            elif c == '#':
                j = s.find('\n', self.i)
                self.i = n if j < 0 else j
            else:
                break

    def ident(self):
        self.ws()
        m = re.compile(r'[A-Za-z_0-9]+').match(self.s, self.i)
        if not m:
            raise SyntaxError('ident expected at %d: %r' % (self.i, self.s[self.i:self.i + 60]))
        self.i = m.end()
        return m.group(0)

    def body(self, node, end='}'):
        while True:
            self.ws()
            if self.i >= self.n:
                return
            c = self.s[self.i]
            if c == end:
                self.i += 1
                self.ws()
                if self.i < self.n and self.s[self.i] == ';':
                    self.i += 1
                return
            if c == ';':
                self.i += 1
                continue
            word = self.ident()
            if word == 'class':
                name = self.ident()
                self.ws()
                base = None
                if self.s[self.i] == ':':
                    self.i += 1
                    base = self.ident()
                    self.ws()
                if self.s[self.i] == ';':
                    self.i += 1
                    node.items.append(('class', Node(name, base)))
                    continue
                if self.s[self.i] != '{':
                    raise SyntaxError('{ expected at %d' % self.i)
                self.i += 1
                child = Node(name, base)
                self.body(child)
                node.items.append(('class', child))
                continue
            self.ws()
            is_array = False
            if self.s.startswith('[]', self.i):
                is_array = True
                self.i += 2
                self.ws()
            if self.s.startswith('+=', self.i):
                self.i += 2
            elif self.s[self.i] == '=':
                self.i += 1
            else:
                raise SyntaxError('= expected at %d: %r' % (self.i, self.s[self.i:self.i + 60]))
            self.ws()
            if is_array or self.s[self.i] == '{':
                val = self.array()
            else:
                val = eval_static(self.raw(';'))
            node.items.append(('prop', word, val))
            self.ws()
            if self.i < self.n and self.s[self.i] == ';':
                self.i += 1

    def raw(self, stops):
        s, start, depth, instr = self.s, self.i, 0, None
        while self.i < self.n:
            c = s[self.i]
            if instr:
                if c == instr:
                    if self.i + 1 < self.n and s[self.i + 1] == instr:
                        self.i += 1
                    else:
                        instr = None
            elif c in '"\'':
                instr = c
            elif c in '([{':
                depth += 1
            elif c in ')]}':
                if depth == 0:
                    if c == '}':
                        break
                    # stray closer, tolerated by the game's parser
                    s = self.s = s[:self.i] + s[self.i + 1:]
                    self.n -= 1
                    continue
                depth -= 1
            elif depth == 0 and c in stops:
                break
            self.i += 1
        return s[start:self.i]

    def array(self):
        self.ws()
        if self.s[self.i] != '{':
            raise SyntaxError('{ expected at %d' % self.i)
        self.i += 1
        out = []
        while True:
            self.ws()
            c = self.s[self.i]
            if c == '}':
                self.i += 1
                return out
            if c == ',':
                self.i += 1
                continue
            if c == '{':
                out.append(self.array())
            else:
                r = self.raw(',}')
                if r.strip():
                    out.append(eval_static(r))


def parse(text):
    root = Node('root')
    Parser(text).body(root, end='\0')
    return root


def find(node, path):
    for name in path:
        node = node.child(name)
        if node is None:
            return None
    return node


def load(path):
    text = open(path, encoding='utf-8').read()
    out, n = [], 0
    for part in re.split(r'(__COUNTER_RESET__|__COUNTER__)', text):
        if part == '__COUNTER_RESET__':
            n = 0
        elif part == '__COUNTER__':
            out.append(str(n))
            n += 1
        else:
            out.append(part)
    return parse(''.join(out))

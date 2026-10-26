
import sys
import re

class Box:
    def __init__(self, lines, mid):
        self.lines = lines
        self.mid = mid
        self.h = len(lines)
        self.w = len(lines[0])

def combine(a, b, op):
    top = max(a.mid, b.mid)
    bottom = max(a.h - a.mid, b.h - b.mid)
    lines = []

    for i in range(top + bottom):
        x = i - top + a.mid
        y = i - top + b.mid

        left = a.lines[x] if 0 <= x < a.h else " " * a.w
        right = b.lines[y] if 0 <= y < b.h else " " * b.w
        middle = f" {op} " if i == top else "   "

        lines.append(left + middle + right)

    return Box(lines, top)

def unary(a):
    lines = []
    for i, line in enumerate(a.lines):
        c = "-" if i == a.mid else " "
        lines.append(c + line)
    return Box(lines, a.mid)

def fraction(a, b):
    w = max(a.w, b.w)

    if a.w < b.w:
        left1 = (w - a.w + 1) // 2
        left2 = 0
    else:
        left1 = 0
        left2 = (w - b.w + 1) // 2

    lines = []
    for line in a.lines:
        lines.append(" " * left1 + line + " " * (w - left1 - a.w))

    lines.append("-" * w)

    for line in b.lines:
        lines.append(" " * left2 + line + " " * (w - left2 - b.w))

    return Box(lines, a.h)

def power(a, b):
    h = a.h + b.h
    w = a.w + b.w
    grid = [[" "] * w for _ in range(h)]

    for i, line in enumerate(a.lines):
        for j, c in enumerate(line):
            grid[b.h + i][j] = c

    for i, line in enumerate(b.lines):
        for j, c in enumerate(line):
            grid[i][a.w + j] = c

    return Box(["".join(row) for row in grid], a.mid + b.h)

def parentheses(a):
    lines = ["(" + line + ")" for line in a.lines]
    return Box(lines, a.h // 2)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def peek(self):
        if self.i >= len(self.tokens):
            return None
        return self.tokens[self.i]

    def next(self):
        t = self.peek()
        self.i += 1
        return t

    def level1(self):
        t = self.next()

        if t == "-":
            return unary(self.level1())

        if t == "{":
            a = self.level5()
            self.next()
            return a

        if t == "(":
            a = self.level5()
            self.next()
            return parentheses(a)

        return Box([t], 0)

    def level2(self):
        a = self.level1()

        if self.peek() == "^":
            self.next()
            b = self.level2()
            a = power(a, b)

        return a

    def level3(self):
        a = self.level2()

        while self.peek() in ("*", "/"):
            op = self.next()
            b = self.level2()

            if op == "*":
                a = combine(a, b, op)
            else:
                a = fraction(a, b)

        return a

    def level4(self):
        a = self.level3()

        while self.peek() in ("+", "-"):
            op = self.next()
            a = combine(a, self.level3(), op)

        return a

    def level5(self):
        a = self.level4()

        while self.peek() == "=":
            self.next()
            a = combine(a, self.level4(), "=")

        return a

def main():
    data = sys.stdin.read()
    tokens = re.findall(r"[A-Za-z0-9.]+|[+\-*/^=(){}]", data)

    parser = Parser(tokens)
    results = []

    while parser.peek() is not None:
        ans = parser.level5()
        results.append("\n".join(ans.lines))

    if results:
        sys.stdout.write("\n\n".join(results) + "\n")

if __name__ == "__main__":
    main()


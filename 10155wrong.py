
import sys

class Box:
    def __init__(self, lines, mid):
        self.lines = lines
        self.mid = mid
        self.h = len(lines)
        self.w = len(lines[0])

def combine(a, b, op):
    top = max(a.mid, b.mid)
    bottom = max(a.h - a.mid - 1, b.h - b.mid - 1)
    h = top + bottom + 1
    lines = []

    for i in range(h):
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
    left1 = (w - a.w + 1) // 2
    left2 = (w - b.w + 1) // 2

    lines = []
    for line in a.lines:
        lines.append(" " * left1 + line + " " * (w - left1 - a.w))

    lines.append("-" * w)

    for line in b.lines:
        lines.append(" " * left2 + line + " " * (w - left2 - b.w))

    return Box(lines, a.h)

def power(a, b):
    top = max(0, b.h - a.mid)
    h = max(top + a.h, b.h)
    w = a.w + b.w
    grid = [[" "] * w for _ in range(h)]

    for i, line in enumerate(a.lines):
        for j, c in enumerate(line):
            grid[top + i][j] = c

    for i, line in enumerate(b.lines):
        row = top + a.mid - b.h + i
        for j, c in enumerate(line):
            grid[row][a.w + j] = c

    return Box(["".join(row) for row in grid], top + a.mid)

def parentheses(a):
    lines = ["(" + line + ")" for line in a.lines]
    return Box(lines, a.h // 2)

class Parser:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def parse(self, limit=0):
        s = self.s

        if s[self.i] == "-":
            self.i += 1
            a = unary(self.parse(6))

        elif s[self.i] in "({":
            c = s[self.i]
            self.i += 1
            a = self.parse()
            self.i += 1
            if c == "(":
                a = parentheses(a)

        else:
            start = self.i
            while self.i < len(s) and (s[self.i].isalnum() or s[self.i] == "."):
                self.i += 1
            a = Box([s[start:self.i]], 0)

        priority = {
            "=": 1,
            "+": 2,
            "-": 2,
            "*": 3,
            "/": 3,
            "^": 5
        }

        while self.i < len(s):
            op = s[self.i]

            if op not in priority:
                break

            p = priority[op]
            if p < limit:
                break

            self.i += 1

            if op == "^":
                b = self.parse(p)
                a = power(a, b)
            else:
                b = self.parse(p + 1)
                if op == "/":
                    a = fraction(a, b)
                else:
                    a = combine(a, b, op)

        return a

def main():
    data = sys.stdin.read().splitlines()
    results = []

    for line in data:
        line = "".join(line.split())
        if not line:
            continue

        ans = Parser(line).parse()
        results.append("\n".join(s.rstrip() for s in ans.lines))

    print("\n\n".join(results))

if __name__ == "__main__":
    main()


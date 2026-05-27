import sys
from math import sqrt, atan2, pi, inf

EPS = 1e-9
O = (0.0, 0.0)
def distance(p, q):
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= EPS:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= EPS:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_length(poly):
    if len(poly) <= 1:
        return 0.0
    total = 0.0
    n = len(poly)
    for i in range(n):
        total += distance(poly[i], poly[(i + 1) % n])
    return total

def on_segment(a, b, p=O):
    return abs(cross(a, b, p)) <= EPS and \
           min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS and \
           min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS

def angle(p):
    a = atan2(p[1], p[0])
    if a < 0:
        a += 2 * pi
    return a

def dist2(p):
    return p[0] * p[0] + p[1] * p[1]

def min_convex_length_with_origin(points):
    pts = []
    for p in set(points):
        if abs(p[0]) <= EPS and abs(p[1]) <= EPS:
            continue
        pts.append(p)
    pts.sort(key=lambda p: (angle(p), dist2(p)))
    n = len(pts)
    best = inf
    for start in range(n):
        stack = [O]
        for k in range(n):
            p = pts[(start + k) % n]
            while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= EPS:
                stack.pop()
            stack.append(p)
        while len(stack) > 2 and cross(stack[-2], stack[-1], O) <= EPS:
            stack.pop()
        length = 0.0
        for i in range(len(stack) - 1):
            length += distance(stack[i], stack[i + 1])
        length += distance(stack[-1], O)
        best = min(best, length)

    return best

def solve(points):
    points.append(O)
    hull = convex_hull(points)
    on_poly = False
    for i in range(len(hull)):
        j = (i + 1) % len(hull)
        if on_segment(hull[i], hull[j], O):
            on_poly = True
            break
    if on_poly:
        return polygon_length(hull) + 2.0
    else:
        return min_convex_length_with_origin(points) + 2.0

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    outputs = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        points = []
        for _ in range(n):
            x = float(data[idx])
            y = float(data[idx + 1])
            idx += 2
            points.append((x, y))
        outputs.append(f"{solve(points):.2f}")
    print("\n\n".join(outputs))
if __name__ == "__main__":
    main()

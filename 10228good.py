from math import sqrt
import sys

def get_dist_sum(x, y, points):
    total = 0.0
    for px, py in points:
        total += sqrt((x-px)**2 + (y-py)**2)
    return total

def calc_y(x, points, low_y, high_y):
    for _ in range(80):
        m1 = low_y + (high_y - low_y) / 3
        m2 = high_y - (high_y - low_y) / 3

        d1 = get_dist_sum(x, m1, points)
        d2 = get_dist_sum(x, m2, points)

        if d1 < d2:
            high_y = m2
        else:
            low_y = m1

    y = (low_y + high_y) / 2
    return get_dist_sum(x, y, points)

def solve(points):
    low_x = min(x for x, y in points)
    high_x = max(x for x, y in points)
    low_y = min(y for x, y in points)
    high_y = max(y for x, y in points)

    for _ in range(80):
        m1 = low_x + (high_x - low_x) / 3
        m2 = high_x - (high_x - low_x) / 3

        d1 = calc_y(m1, points, low_y, high_y)
        d2 = calc_y(m2, points, low_y, high_y)

        if d1 < d2:
            high_x = m2
        else:
            low_x = m1

    x = (low_x + high_x) / 2
    ans = calc_y(x, points, low_y, high_y)

    return int(ans + 0.5)

def main():
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx])
    idx += 1

    ans = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        points = []
        for _ in range(n):
            x = float(data[idx])
            y = float(data[idx + 1])
            idx += 2
            points.append((x, y))

        ans.append(str(solve(points)))

    print("\n\n".join(ans))

if __name__ == "__main__":
    main()

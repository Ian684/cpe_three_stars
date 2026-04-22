import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        num_scenarios = int(next(it))
    except StopIteration:
        return
    for _ in range(num_scenarios):
        l = int(next(it))
        w = int(next(it))
        tree_points = set()
        y_coords = {0, w}
        while True:
            k = int(next(it))
            if k == 0: break
            tx = int(next(it))
            ty = int(next(it))
            if k == 1:
                tree_points.add((tx, ty))
                y_coords.add(ty)
            else:
                dx = int(next(it))
                dy = int(next(it))
                for i in range(k):
                    cx, cy = tx + i*dx, ty + i*dy
                    tree_points.add((cx, cy))
                    y_coords.add(cy)
        for y in y_coords:
            tree_points.add((0, y))
        trees = sorted(list(tree_points))
        ans = 0
        num_t = len(trees)
        for i in range(num_t):
            t1 = trees[i]
            x1, y1 = t1[0], t1[1]
            upper, lower = w, 0
            for j in range(i + 1, num_t):
                t2 = trees[j]
                x2, y2 = t2[0], t2[1]
                if x2 > x1:
                    current_w = upper - lower
                    area = (x2 - x1) * current_w
                    if area > ans:
                        ans = area
                if y2 == y1:
                    upper = lower
                    break
                elif y2 > y1:
                    if y2 < upper:
                        upper = y2
                else:
                    if y2 > lower:
                        lower = y2
                if upper <= lower:
                    break
            if upper > lower:
                area = (l - x1) * (upper - lower)
                if area > ans:
                    ans = area
        sorted_y = sorted(list(y_coords))
        for i in range(len(sorted_y) - 1):
            area = l * (sorted_y[i+1] - sorted_y[i])
            if area > ans:
                ans = area
        sys.stdout.write(str(ans) + '\n')
if __name__ == "__main__":
    solve()

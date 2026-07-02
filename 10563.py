import sys

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def can_place(grid, m, n, r, c, size, ch):
    if r + size > m or c + size > n:
        return False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if grid[i][j] != '?':
                return False

    bottom = r + size - 1
    right = c + size - 1
    for j in range(c, right + 1):
        if r > 0 and grid[r - 1][j] == ch:
            return False
        if bottom + 1 < m and grid[bottom + 1][j] == ch:
            return False
    for i in range(r, bottom + 1):
        if c > 0 and grid[i][c - 1] == ch:
            return False
        if right + 1 < n and grid[i][right + 1] == ch:
            return False

    return True

def smallest_char(grid, m, n, r, c):
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ok = True
        for dr, dc in DIRS:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == ch:
                    ok = False
                    break
        if ok:
            return ch
    return 'Z'

def can_use_char_at(grid, m, n, r, c, ch):
    if not (0 <= r < m and 0 <= c < n):
        return False
    if grid[r][c] != '?':
        return False
    for dr, dc in DIRS:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < m and 0 <= nc < n:
            if grid[nr][nc] == ch:
                return False
    return True

def smaller_possible_after(grid, m, n, r, c, cur_ch):
    if not (0 <= r < m and 0 <= c < n):
        return False

    if grid[r][c] != '?':
        return False

    for code in range(ord('A'), ord(cur_ch)):
        ch = chr(code)
        if can_use_char_at(grid, m, n, r, c, ch):
            return True

    return False


def solve_case(m, n, lines):
    grid = [list(row) for row in lines]

    for i in range(m):
        for j in range(n):
            if grid[i][j] != '?':
                continue
            ch = smallest_char(grid, m, n, i, j)
            size = 1
            while True:
                if smaller_possible_after(grid, m, n, i, j + size, ch):
                    break
                if can_place(grid, m, n, i, j, size + 1, ch):
                    size += 1
                else:
                    break
            for r in range(i, i + size):
                for c in range(j, j + size):
                    grid[r][c] = ch

    return ["".join(row) for row in grid]

def main():
    data = sys.stdin.read().splitlines()
    idx = 0
    outputs = []

    while idx < len(data):
        m, n = map(int, data[idx].split())
        idx += 1

        if m == 0 and n == 0:
            break

        lines = data[idx:idx + m]
        idx += m

        outputs.append("\n".join(solve_case(m, n, lines)))

    print("\n\n".join(outputs))


if __name__ == "__main__":
    main()

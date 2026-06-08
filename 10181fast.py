import sys

aim = (1,2,3,4,
       5,6,7,8,
       9,10,11,12,
       13,14,15,0)

directions = (
    (-1, 0, 'U'),
    (1, 0, 'D'),
    (0, -1, 'L'),
    (0, 1, 'R')
)

opposite = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}
goal_x = [0] * 16
goal_y = [0] * 16
for num in range(1, 16):
    pos = num - 1
    goal_x[num] = pos // 4
    goal_y[num] = pos % 4

def tile_dis(num, pos):
    if num == 0:
        return 0
    x = pos // 4
    y = pos % 4
    return abs(x - goal_x[num]) + abs(y - goal_y[num])

def get_h(block):
    count = 0
    for i in range(16):
        num = block[i]
        if num == 0:
            continue
        count += tile_dis(num, i)
    return count

def inversion(block):
    count = 0
    for i in range(16):
        if block[i] == 0:
            continue
        for j in range(i + 1, 16):
            if block[j] == 0:
                continue
            if block[i] > block[j]:
                count += 1
    zero = block.index(0)
    row_from_bottom = 4 - zero // 4
    return (count + row_from_bottom) % 2 == 1

def ida_star(arr):
    block = arr[:]
    zero = block.index(0)
    h = get_h(block)
    bound = h
    path = []
    def dfs(zero, step, h, bound, last_move):
        f = step + h
        if f > bound:
            return f
        if h == 0:
            return True

        if step >= 50:
            return float("inf")

        min_next_bound = float("inf")

        x = zero // 4
        y = zero % 4

        for dx, dy, d in directions:
            if last_move and opposite[last_move] == d:
                continue

            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue

            new_zero = nx * 4 + ny

            num = block[new_zero]
            old_dis = tile_dis(num, new_zero)
            new_dis = tile_dis(num, zero)

            new_h = h - old_dis + new_dis

            block[zero], block[new_zero] = block[new_zero], block[zero]
            path.append(d)

            result = dfs(new_zero, step + 1, new_h, bound, d)

            if result is True:
                return True

            if result < min_next_bound:
                min_next_bound = result

            path.pop()
            block[zero], block[new_zero] = block[new_zero], block[zero]

        return min_next_bound

    while bound <= 50:
        result = dfs(zero, 0, h, bound, "")

        if result is True:
            return "".join(path)

        if result == float("inf"):
            return None

        bound = result
    return None

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        temp = data[idx:idx + 16]
        idx += 16
        if not inversion(temp):
            ans.append("This puzzle is not solvable.")
            continue
        result = ida_star(temp)
        if result is None:
            ans.append("This puzzle is not solvable.")
        else:
            ans.append(result)
    print("\n".join(ans))
if __name__ == "__main__":
    main()

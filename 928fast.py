import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        num_test_cases = int(next(it))
    except StopIteration:
        return
    for _ in range(num_test_cases):
        R = int(next(it))
        C = int(next(it))
        grid = [next(it) for _ in range(R)]
        start_pos = None
        end_pos = None
        is_wall = [[False] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                char = grid[r][c]
                if char == 'S':
                    start_pos = (r, c)
                elif char == 'E':
                    end_pos = (r, c)
                elif char == '#':
                    is_wall[r][c] = True
        visited = [[[False] * C for _ in range(R)] for _ in range(3)]
        queue = deque([(start_pos[0], start_pos[1], 0, 0)])
        visited[0][start_pos[0]][start_pos[1]] = True
        found = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        step_sizes = [1, 2, 3]
        while queue:
            r, c, s_idx, moves = queue.popleft()
            if (r, c) == end_pos:
                print(moves)
                found = True
                break
            step_dist = step_sizes[s_idx]
            next_s_idx = (s_idx + 1) % 3
            for dr, dc in directions:
                nr, nc = r, c
                can_move = True
                for _ in range(step_dist):
                    nr += dr
                    nc += dc
                    if not (0 <= nr < R and 0 <= nc < C) or is_wall[nr][nc]:
                        can_move = False
                        break
                if can_move and not visited[next_s_idx][nr][nc]:
                    visited[next_s_idx][nr][nc] = True
                    queue.append((nr, nc, next_s_idx, moves + 1))
        if not found:
            print("NO")
if __name__ == "__main__":
    solve()

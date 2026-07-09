from collections import deque
from math import *

def get_dis_bfs(m , n , arr , startx , starty , l):

    q = deque([])
    step = 0
    q.append([startx , starty , step])
    check = [[False]*n for _ in range(m)]
    check[startx][starty] = True
    directions = ((0,-1),(0,1),(1,0),(-1,0))
    dis = [1 << 60]*l

    while q:
        nowx , nowy , step = q.popleft()
        for dx , dy in directions:
            nx , ny = nowx + dx , nowy + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:continue
            if check[nx][ny]:continue
            if arr[nx][ny] == '#':continue
            if arr[nx][ny] not in ('.' , '#' , 'X' , 'O'):
                dis[arr[nx][ny]] = step+1
            check[nx][ny] = True
            q.append([nx , ny , step+1])

    return dis

def bitmask_dp(s_dis , guards_dis , treasures_dis , l):

    dp = [[1 << 60]*l for _ in range(1 << l)]
    mask = 0

    for j in range(l):
        dp[mask][j] = 0
        if s_dis[j] + 1 >= guards_dis[j]:continue
        dp[mask | (1 << j)][j] = s_dis[j] + 1

    for mask in range(1 , 1 << l):
        for i in range(l):
            if dp[mask][i] >= 1 << 60:
                continue
            for j in range(l):
                if (mask & (1 << j)):
                    continue
                next_time = dp[mask][i] + treasures_dis[i][j] + 1
                if next_time >= guards_dis[j]:
                    continue
                next_mask = mask | (1 << j)
                dp[next_mask][j] = min(next_time , dp[next_mask][j])

    biggest_treasure = -1
    smallest_time = 1 << 60
    for mask in range(1 << l):
        if min(dp[mask]) >= 1 << 60:continue
        now_treasure = bin(mask)[2:].count('1')
        if now_treasure > biggest_treasure:
            biggest_treasure = now_treasure
            smallest_time = min(dp[mask])
        elif now_treasure == biggest_treasure:
            smallest_time = min(smallest_time , min(dp[mask]))

    return biggest_treasure , smallest_time

def solve(m , n , arr):

    guards = []
    treasures = []
    sx , sy = None , None
    count = 0

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 'O':
                sx , sy = i , j
            elif arr[i][j] == 'X':
                guards.append([i , j])
            elif arr[i][j] != '.' and arr[i][j] != '#':
                treasures.append([i , j])
                arr[i][j] = count
                count += 1

    l = len(treasures)
    if l == 0:
        return 0 , 0

    s_dis = get_dis_bfs(m , n , arr , sx , sy , l)

    guards_dis = [1 << 60]*l
    for i in range(len(guards)):
        temp = get_dis_bfs(m , n , arr , guards[i][0] , guards[i][1] , l)
        for j in range(l):
            guards_dis[j] = min(guards_dis[j] , temp[j])

    treasures_dis = [[-1]*l for _ in range(l)]
    for i in range(l):
        temp = get_dis_bfs(m , n , arr , treasures[i][0] , treasures[i][1] , l)
        for j in range(l):
            treasures_dis[i][j] = temp[j]

    treasure , time = bitmask_dp(s_dis , guards_dis , treasures_dis , l)
    return treasure , time
    
def main():

    now = 1
    while True:
        try:
            m , n = map(int , input().split())
            arr = [[None]*n for _ in range(m)]
            count = 0
            for i in range(m):
                temp = input()
                for j in range(n):
                    arr[i][j] = temp[j]
        except EOFError:break

        treasure , time = solve(m , n , arr)
        print(f"Case {now}:")
        if treasure == 0:
            print("No treasures can be collected.\n")
        else:
            print(f"Maximum number of collectible treasures: {treasure}.")
            print(f"Minimum Time: {time} sec.\n")
        now += 1

if __name__ == "__main__":
    main()

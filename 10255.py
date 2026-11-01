def solve(n , x , y):

    if n % 2 == 1 or n < 6:return None

    directions = (
        (-1,-2), (-2,-1), (-2,1), (-1,2),
        (1,2), (2,1), (2,-1), (1,-2)
    )
    center = (n+1) // 2 - 1

    # 可以嘗試不同排序，因為當ndis == mdis會出現不同可能性
    # 也可以用dfs去嘗試temp == m and ndis == mdis的可能方向
    for shift in range(8):
        moves = directions[shift:] + directions[:shift]
        ans = [[0]*n for _ in range(n)]
        i , j = x-1 , y-1
        ans[i][j] = 1
        flag = True
    
        for count in range(2 , n*n+1):
            mx , my = -1 , -1
            m = 1 << 32

            for dx , dy in moves:
                nx , ny = i + dx , j + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
                if ans[nx][ny]:continue

                temp = 0
                for ddx , ddy in directions:
                    nnx , nny = nx + ddx , ny + ddy
                    if nnx < 0 or nny < 0 or nnx >= n or nny >= n:continue
                    if not ans[nnx][nny]:
                        temp += 1
                if temp < m:
                    m = temp
                    mx , my = nx , ny
                elif temp == m:
                    ndis = abs(nx - center) + abs(ny - center)
                    mdis = abs(mx - center) + abs(my - center)
                    if ndis > mdis:
                        mx , my = nx , ny

            if m == 1 << 32 and mx == -1 and my == -1:
                flag = False
                break
            ans[mx][my] = count
            i , j = mx , my
        if flag:
            return ans
    return None

def main():

    first = True
    while True:

        try:
            n , x , y = map(int , input().split())
        except EOFError:break

        ans = solve(n , x , y)
        if first:first = False
        else:print()
        if ans is None:print("No Circuit Tour.")
        else:
            for i in range(n):
                for j in range(n):
                    print(' '*(5-len(str(ans[i][j])))+str(ans[i][j]) , end='')
                print()

if __name__ == "__main__":
    main()

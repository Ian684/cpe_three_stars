def main():
    first = True
    now = 0
    while True:
        c , r , q = map(int , input().split())
        if c == 0 and r == 0 and q == 0:break
        fee = list(map(int , input().split()))
        cities = sorted(range(c) , key = lambda x : fee[x])
        dp = [[1 << 32]*c for i in range(c)]
        ans = [[1 << 32]*c for i in range(c)]
        for i in range(r):
            a , b , d = map(int , input().split())
            a -= 1
            b -= 1
            dp[a][b] = d
            dp[b][a] = d

        for i in range(c):
            dp[i][i] = 0

        for k in cities:
            for i in range(c):
                for j in range(c):
                    dp[i][j] = min(dp[i][j] , dp[i][k]+dp[k][j])

            for i in range(c):
                for j in range(c):
                    ans[i][j] = min(ans[i][j] , dp[i][j] + max(fee[i] , fee[k] , fee[j]))
        if first:first = False
        else:print()
        print(f"Case #{now+1}")
        now += 1
        for i in range(q):
            a , b = map(int , input().split())
            a -= 1
            b -= 1
            if ans[a][b] == 1 << 32:
                print(-1)
            else:
                print(ans[a][b])

if __name__ == "__main__":
    main()

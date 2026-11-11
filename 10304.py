def main():
    while True:
        try:
            line = list(map(int , input().split()))
        except EOFError:break
        n , arr = line[0] , line[1:]
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            cost[i][i] = arr[i]
        for l in range(2 , n+1):
            for i in range(n-l+1):
                j = i + l - 1
                for k in range(i , j+1):
                    cost[i][j] += arr[k]

        dp = [[1 << 32]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for l in range(2 , n+1):
            for i in range(n-l+1):
                j = i + l - 1
                for k in range(i , j+1):
                    if k == i:
                        dp[i][j] = min(dp[i][j] , dp[k+1][j] + cost[i][j] - arr[k])
                        continue
                    if k == j:
                        dp[i][j] = min(dp[i][j] , dp[i][k-1] + cost[i][j] - arr[k])
                        continue
                    dp[i][j] = min(dp[i][j] , dp[i][k-1] + dp[k+1][j] + cost[i][j] - arr[k])

        print(dp[0][n-1])

if __name__ == "__main__":
    main()

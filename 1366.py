def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        preY = [[0]*m for _ in range(n)]
        for i in range(n):
            line = list(map(int , input().split()))
            c = 0
            for j in range(m):
                c += line[j]
                preY[i][j] = c
        c = [0]*m
        preB = [[0]*m for _ in range(n)]
        for i in range(n):
            line = list(map(int , input().split()))
            for j in range(m):
                c[j] += line[j]
                preB[i][j] = c[j]
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = max(preY[0][0] , preB[0][0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:continue
                if i - 1 < 0:
                    dp[i][j] = max(preY[i][j] , dp[i][j-1]+preB[i][j])
                elif j - 1 < 0:
                    dp[i][j] = max(dp[i-1][j]+preY[i][j] , preB[i][j])
                dp[i][j] = max(dp[i-1][j]+preY[i][j] , dp[i][j-1]+preB[i][j])
        print(dp[-1][-1])
if __name__ == "__main__":
    main()

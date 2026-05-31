def main():
    while True:
        try:
            line = input()
            if line == "":continue
            n , d = map(int , line.split())
            if n & 1:
                print(0)
                continue
            if n//2 < d:
                print(0)
                continue
        except EOFError:break
        dp = [[0]*(d+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(d+1):
                if j < d:
                    # put left parent
                    dp[i+1][j+1] += dp[i][j]
                if j > 0:
                    # put right parent
                    dp[i+1][j-1] += dp[i][j]
        ans = dp[n][0]
        dp = [[0]*(d) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(d):
                if j < d-1:
                    dp[i+1][j+1] += dp[i][j]
                if j > 0:
                    dp[i+1][j-1] += dp[i][j]
        ans -= dp[n][0]
        print(ans)

if __name__ == "__main__":
    main()

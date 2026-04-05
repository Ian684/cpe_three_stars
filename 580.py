def main():
    while True:
        n = int(input())
        if n == 0:break
        if n == 1 or n == 2:
            print(0)
            continue
        dp = [[0]*(n+1) for _ in range(2)]
        dp[0][1] = 1
        dp[1][1] = 1
        dp[0][2] = 2
        dp[1][2] = 2
        for i in range(3 , n+1):
            dp[0][i] = dp[0][i-1] + dp[1][i-1]
            dp[1][i] = dp[0][i-1] + dp[0][i-2]
        print(2**n - dp[0][n] - dp[1][n])
if __name__ == "__main__":
    main()

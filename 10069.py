def main():
    c = int(input())
    for _ in range(c):
        x = input()
        z = input()
        dp = [[0]*len(x) for i in range(len(z))]
        if x[0] == z[0]:dp[0][0] = 1
        for j in range(1 , len(x)):
            if z[0] == x[j]:
                dp[0][j] = dp[0][j-1] + 1
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1 , len(z)):
            for j in range(1 , len(x)):
                if x[j] == z[i]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp[-1][-1])
if __name__ == "__main__":
    main()

def main():
    while True:
        try:
            k , n = map(int , input().split())
        except EOFError:break
        k += 1
        total = k**n
        dp = [[0]*k for _ in range(n)]
        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[i][j] = 1
                else:
                    count = dp[i-1][j]
                    if j + 1 < k:
                        count += dp[i-1][j+1]
                    if j - 1 >= 0:
                        count += dp[i-1][j-1]
                    dp[i][j] = count
        count = 0
        for i in range(k):
            count += dp[-1][i]
        print(f"{count/total*100:.5f}")
if __name__ == "__main__":
    main()

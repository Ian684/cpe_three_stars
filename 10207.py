def main():
    first = True
    while True:
        p , n = input().split()
        n = int(n)
        if n == 0:break
        p = float(p)
        q = 1 - p
        dp = [[0]*1001 for _ in range(1001)]
        count = [[0]*1001 for _ in range(1001)]
        for i in range(1001):
            for j in range(1001):
                if i == 0:
                    dp[i][j] = 1
                    count[i][j] = 1
                elif j == 0:
                    dp[i][j] = 0
                    count[i][j] = 1
                else:
                    dp[i][j] = p*dp[i-1][j] + q*dp[i][j-1]
                    count[i][j] = count[i-1][j] + count[i][j-1] + 1
        dp[0][0] = -1
        if first:first = False
        else:print()
        for i in range(n):
            a , b = map(int , input().split())
            print(f"{dp[a][b]:.5f}")
            print(f"{count[a][b]-1}")

if __name__ == "__main__":
    main()

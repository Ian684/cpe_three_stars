def main():
    test = int(input())
    for _ in range(test):
        k , n = map(int , input().split())
        k += 8
        arr = [None] + list(map(int , input().split()))[::-1]
        
        dp = [[1 << 32]*(k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(2 , n+1):
            for j in range(1 , k+1):
                if (i-2)-3*(j-1) >= 1:
                    dp[i][j] = min(dp[i-1][j] , dp[i-2][j-1] + (arr[i]-arr[i-1])**2)
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp[n][k])

if __name__ == "__main__":
    main()

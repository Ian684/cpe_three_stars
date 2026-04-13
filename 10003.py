def main():
    while True:
        ll = int(input())
        if ll == 0:break
        n = int(input())
        arr = [0]+list(map(int , input().split()))+[ll]
        dp = [[1 << 60]*(n+2) for _ in range(n+2)]
        for i in range(n+1):
            dp[i][i+1] = 0
        for l in range(2 , n+2):
            for i in range(n-l+2):
                j = i + l
                for k in range(i+1 , j):
                    dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k][j] + arr[j] - arr[i])
        print(f"The minimum cutting is {dp[0][n+1]}.")
if __name__ == "__main__":
    main()

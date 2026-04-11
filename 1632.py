import sys
def main():
    tokens = sys.stdin.read().split()
    tokens = iter(tokens)
    while True:
        n = int(next(tokens))
        places = []
        time = []
        for i in range(n):
            place , limit_time = int(next(tokens)) , int(next(tokens))
            places.append(place)
            time.append(limit_time)
        dp = [[[1 << 60]*2 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i][0] = 0
            dp[i][i][1] = 0
        for l in range(2 , n+1):
            for i in range(n-l+1):
                j = i + l - 1
                temp = dp[i+1][j][0] + abs(places[i] - places[i+1])
                if temp < time[i]:dp[i][j][0] = min(dp[i][j][0] , temp)
                temp = dp[i][j-1][1] + abs(places[j] - places[j-1])
                if temp < time[j]:dp[i][j][1] = min(dp[i][j][1] , temp)
                temp = dp[i+1][j][1] + abs(places[i] - places[j])
                if temp < time[i]:dp[i][j][0] = min(dp[i][j][0] , temp)
                temp = dp[i][j-1][0] + abs(places[i] - places[j])
                if temp < time[j]:dp[i][j][1] = min(dp[i][j][1] , temp)
        ans = min(dp[0][n-1])
        if ans >= 1 << 60:
            print("No solution")
        else:
            print(ans)
if __name__ == "__main__":
    main()

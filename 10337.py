def main():
    test = int(input())
    for _ in range(test):
        while True:
            line = input()
            if line != '':break
        high = 10
        x = int(line) // 100
        arr = [[] for i in range(x)]
        for i in range(high):
            temp = list(map(int , input().split()))
            for j in range(x):
                arr[j].append(temp[j])
        for i in range(x):
            arr[i] = arr[i][::-1]
        move = [20 , 30 , 60]

        dp = [[1 << 32]*high for i in range(x+1)]
        dp[0][0] = 0

        for i in range(1 , x+1):
            for j in range(high):
                if j > 0:
                    dp[i][j] = min(dp[i][j] , dp[i-1][j-1] + move[2] - arr[i-1][j-1])
                dp[i][j] = min(dp[i][j] , dp[i-1][j] + move[1] - arr[i-1][j])
                if j < high - 1:
                    dp[i][j] = min(dp[i][j] , dp[i-1][j+1] + move[0] - arr[i-1][j+1])

        print(dp[x][0])
        print()

if __name__ == "__main__":
    main()

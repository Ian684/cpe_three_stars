def main():
    while True:
        try:
            n = int(input())
        except EOFError:break
        coins = {1:1,2:2,3:3,4:1}
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(n+1):
            for k , v in coins.items():
                if i - v >= 0:
                    dp[i] += dp[i-v]
        print(dp[n])

if __name__ == "__main__":
    main()

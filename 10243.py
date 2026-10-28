def solve(n , lines):
    
    dp = [[0 , 1] for i in range(n)]

    def dfs(now , parent):

        for _next in lines[now]:
            if _next == parent:continue

            dfs(_next , now)

            dp[now][0] += dp[_next][1]
            dp[now][1] += min(dp[_next])

    dfs(0 , -1)
    return dp

def main():

    while True:

        n = int(input())
        if n == 0:break
        lines = [[] for _ in range(n)]

        for i in range(n):
            for l in list(map(int , input().split()[1:])):
                lines[i].append(l-1)

        dp = solve(n , lines)
        ans = min(dp[0])
        if n == 1:
            ans = 1
        print(ans)


if __name__ == "__main__":
    main()

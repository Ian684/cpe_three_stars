import sys

def solve(n, s, arr):
    dp = [[1 << 32]*(s+1) for _ in range(s+1)]
    dp[0][0] = 0
    for a, b in arr:
        for i in range(a, s+1):
            for j in range(b, s+1):
                dp[i][j] = min(dp[i][j], dp[i-a][j-b] + 1)

    ans = 1 << 32
    for i in range(s+1):
        for j in range(s+1):
            if i**2 + j**2 == s**2:
                ans = min(ans, dp[i][j])

    if ans == 1 << 32:
        return "not possible"
    return ans

def main():
    data = iter(map(int, sys.stdin.read().split()))

    test = next(data)
    for case in range(test):
        n = next(data)
        s = next(data)
        arr = []
        for i in range(n):
            a = next(data)
            b = next(data)
            arr.append([a, b])

        ans = solve(n, s, arr)
        print(ans)

if __name__ == "__main__":
    main()

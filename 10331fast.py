from heapq import *
import sys

def solve(n, l, lines):
    ans = [0] * l
    INF = 1 << 60

    for s in range(n):
        dis = [INF] * n
        dis[s] = 0
        hq = [(0, s)]

        while hq:
            d, u = heappop(hq)

            if d != dis[u]:
                continue

            for v, w, i in lines[u]:
                nd = d + w

                if nd < dis[v]:
                    dis[v] = nd
                    heappush(hq, (nd, v))

        order = sorted(
            (u for u in range(n) if dis[u] != INF),
            key=lambda u: dis[u],
            reverse=True
        )

        dp = [0] * n

        for u in order:
            dp[u] = 1 << u

            for v, w, i in lines[u]:
                if dis[v] != INF and dis[u] + w == dis[v]:
                    dp[u] |= dp[v]

        mask = ((1 << n) - 1) ^ ((1 << (s + 1)) - 1)

        for u in order:
            for v, w, i in lines[u]:
                if dis[v] != INF and dis[u] + w == dis[v]:
                    ans[i] += bin(dp[v] & mask).count('1')

    m = max(ans)
    return [str(i + 1) for i in range(l) if ans[i] == m]


def main():
    input = sys.stdin.readline

    while True:
        line = input()
        if not line:
            break

        if not line.strip():
            continue

        n, l = map(int, line.split())

        lines = [[] for _ in range(n)]

        for i in range(l):
            a, b, d = map(int, input().split())
            a -= 1
            b -= 1

            lines[a].append((b, d, i))
            lines[b].append((a, d, i))

        if l == 0:
            print()
            continue

        print(' '.join(solve(n, l, lines)))


if __name__ == "__main__":
    main()

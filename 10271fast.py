
import sys

def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    test = next(data)

    for _ in range(test):
        k = next(data) + 8
        n = next(data)

        arr = sorted(
            (next(data) for _ in range(n)),
            reverse=True
        )

        cost = [0, 0] + [
            (arr[i-1] - arr[i-2])**2
            for i in range(2, n+1)
        ]

        INF = 1 << 60
        prev = [0] * (n+1)

        for j in range(1, k+1):
            curr = [INF] * (n+1)

            end = n - 2*(k-j) + 1

            for i in range(3*j, end):
                curr[i] = min(curr[i-1] , prev[i-2] + cost[i])

            prev = curr

        print(prev[n])

if __name__ == "__main__":
    main()


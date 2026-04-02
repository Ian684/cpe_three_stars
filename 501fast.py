import sys
from heapq import *
def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    N = int(next(tokens))
    for a in range(N):
        m = int(next(tokens))
        n = int(next(tokens))
        arr = []
        urr = []
        v = {}
        for r in range(m):
            arr.append(int(next(tokens)))
            v[r+1] = 0
        for r in range(n):
            temp = int(next(tokens))
            urr.append(temp)
            v[temp] += 1
        small , big = [] , []
        for i in range(m):
            heappush(small , -arr[i])
            heappush(big , -heappop(small))
            while v[i+1]:
                t = heappop(big)
                print(t)
                heappush(small , -t)
                v[i+1] -= 1
        if a != N - 1:print()
if __name__ == "__main__":
    main()

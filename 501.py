import sys
import bisect
def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    N = int(next(tokens))
    for a in range(N):
        m = int(next(tokens))
        n = int(next(tokens))
        arr = []
        urr = []
        for r in range(m):
            arr.append(int(next(tokens)))
        for r in range(n):
            urr.append(int(next(tokens)))
        i = 0
        l = 1
        u = 0
        if m != 0:
            stack = [arr[0]]
            for time in range(1 , m):
                while u < n and urr[u] == l:
                    i += 1
                    u += 1
                    print(stack[i-1])
                bisect.insort(stack , arr[time])
                l += 1
            while u < n and urr[u] == l:
                i += 1
                u += 1
                print(stack[i-1])
        if a != N - 1:print()
if __name__ == "__main__":
    main()

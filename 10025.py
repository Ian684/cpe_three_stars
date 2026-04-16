import sys
from math import *

def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    c = int(next(tokens))
    for i in range(c):
        k = abs(int(next(tokens)))
        if k == 0:
            print(3)
            if i != c-1:print()
            continue
        n = ceil((-1+sqrt(1+8*k)) / 2)
        while True:
            if not (((n+1)*n//2)-k & 1):
                break
            n += 1
        print(n)
        if i != c-1:print()
if __name__ == "__main__":
    main()

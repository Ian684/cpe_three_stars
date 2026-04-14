from math import *

def main():
    n = int(input())
    for _ in range(n):
        trash = input()
        m , n = map(int , input().split())
        ml = int(ceil(sqrt(m)))
        nl = int(ceil(sqrt(n)))
        mleft , mright = (ml-1)**2 + 1 , (ml)**2
        nleft , nright = (nl-1)**2 + 1 , (nl)**2
        print(mleft , mright)
        ans = abs(nl - ml) + abs((n - nleft)//2 - (m - mleft)//2) + abs((nright - n)//2 - (mright-m)//2)
        print(ans)
        if _ != n - 1:print()
if __name__ == "__main__":
    main()

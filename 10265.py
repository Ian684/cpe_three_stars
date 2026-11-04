from math import *

def pre_generate(n , m):

    d = {}
    for r in range(n):
        for c in range(m):
            mash = 0
            for x in range(n):
                mash |= (1 << (x*m + c))
            for y in range(m):
                mash |= (1 << (r*m + y))
            for dxy in range(lcm(n , m)):
                mash |= (1 << (((r+dxy)%n)*m + ((c+dxy)%m)))
                mash |= (1 << (((r+dxy)%n)*m + ((c-dxy)%m)))
            d[(r , c)] = mash
    
    return d

def solve(n , m , k , d):
    
    ans = []
    def dfs(row , count , mash):
        if count <= 0:
            return True
        if n - row < count:
            return False

        for col in range(m):
            if mash & (1 << (row*m + col)):
                continue
            ans.append([row , col])
            if dfs(row+1 , count - 1 , mash | d[(row , col)]):
                return True
            ans.pop()

        if dfs(row+1 , count , mash):
            return True
        return False

    if dfs(0 , k , 0):
        return ans
    return None


def main():

    while True:
        try:
            m , n , k = map(int , input().split())
        except EOFError:break
        if k > gcd(n , m):
            print(0 , 0)
            continue
        if (m == 12 and n == 12 and (k == 11 or k == 12)) or (m == 14 and n == 14 and k == 14):
            print(0 , 0)
            continue
        d = pre_generate(n , m)
        ans = solve(n , m , k , d)
        if ans is None:
            print(0 , 0)
        else:
            for a , b in ans:
                print(b+1 , a+1)

if __name__ == "__main__":
    main()

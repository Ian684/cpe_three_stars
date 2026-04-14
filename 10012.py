from math import *
ans = None

def solve(c , q , circles , now , check , x , r):
    global ans
    if c >= q:
        ans = min(ans , x+r)
    for _next in range(q):
        if check[_next]:continue
        check[_next] = True
        solve(c+1 , q , circles , _next , check , x + sqrt((circles[_next]+circles[now])**2-(circles[_next]-circles[now])**2) , circles[_next])
        check[_next] = False
    return 

def main():
    global ans
    n = int(input())
    for _ in range(n):
        line = input().split()
        q = int(line[0])
        circles = list(map(float , line[1:]))
        ans = 1 << 60
        for i in range(q):
            check = [False]*q
            check[i] = True
            solve(1 , q , circles , i , check , circles[i] , circles[i])
        print(f"{ans:.3f}")
if __name__ == "__main__":
    main()

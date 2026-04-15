from math import *
import sys
sys.setrecursionlimit(200000)
ans = None

def solve(c , q , circles , now , current_circles , x_all):
    global ans
    if c >= q:
        temp = -1
        for j in range(q):
            temp = max(temp , circles[current_circles[j]]+x_all[j])
        ans = min(ans , temp)
    for _next in range(q):
        if _next in current_circles:continue
        next_x = circles[_next]
        
        for j in range(len(x_all)):
            num , temp_x = current_circles[j] , x_all[j]
            next_x = max(next_x , temp_x + 2*sqrt(circles[num]*circles[_next]))
        x_all.append(next_x)
        current_circles.append(_next)    
        solve(c+1 , q , circles , _next , current_circles , x_all)
        current_circles.pop()    
        x_all.pop()
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
            current_circles = [i]
            x_all = [circles[i]]
            solve(1 , q , circles , i , current_circles , x_all)
        print(f"{ans:.3f}")
if __name__ == "__main__":
    main()

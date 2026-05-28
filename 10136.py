from math import *

EPS = 1e-6

def cal_points(points , x , y):
    total = 0
    n = len(points)
    for i in range(n):
        x1 , y1 = points[i]
        if (x1-x)**2 + (y1-y)**2 <= 6.25 + EPS:
            total += 1
    return total

def main():
    t = int(input())
    blank_line = input()
    for c in range(t):
        points = []
        while True:
            try:
                line = input()
                if line == "": break
                points.append(list(map(float , line.split())))
            except EOFError: break
        n = len(points)
        ans = 1
        for i in range(n):
            for j in range(i+1,n):
                x1 , y1 = points[i]
                x2 , y2 = points[j]

                dx , dy = x2 - x1 , y2 - y1
                d = dx*dx + dy*dy
                
                if d > 25 + EPS: continue
                midx , midy = (x2+x1)/2 , (y2+y1)/2
                d = sqrt(d)
                h = sqrt(2.5**2-(d/2)**2)

                cx , cy = midx + h * (dy/d) , midy - h * (dx/d)
                ans = max(ans , cal_points(points , cx , cy))
                cx , cy = midx - h * (dy/d) , midy + h * (dx/d)
                ans = max(ans , cal_points(points , cx , cy))
        print(ans)
        if c != t-1: print()

if __name__ == "__main__":
    main()

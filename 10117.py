# use line equation and find all points in one side of it
# the key is direction (it gives us anti_clockwise points , so the inner is right of the line)
from math import *

def cal_area(points):
    n = len(points)
    if n < 3:return 0.0
    result = 0.0
    for i in range(n):
        j = (i+1)%n
        result += points[i][0]*points[j][1] - points[i][1]*points[j][0]
    return abs(result) / 2.0

def Sutherland_Hodgman(points , a , b , c):
    new_points = []
    if not points:return []

    n = len(points)
    for i in range(n):
        j = (i+1)%n
        x1 , y1 = points[i]
        x2 , y2 = points[j]

        d1 = a*x1 + b*y1 + c
        d2 = a*x2 + b*y2 + c

        if d2 >= -1e-9:
            if d1 < -1e-9:
                t = d1 / (d1 - d2)
                new_points.append([x1 + t*(x2-x1) , y1 + t*(y2-y1)])
            new_points.append([x2 , y2])
        elif d1 >= -1e-9:
            if d2 < -1e-9:
                t = d1 / (d1 - d2)
                new_points.append([x1 + t*(x2-x1) , y1 + t*(y2-y1)])

    return new_points

def solve(n , k , h , points):
    
    total_area = cal_area(points)
    planes = []
    for i in range(n):
        j = (i+1)%n
        x1 , y1 = points[i]
        x2 , y2 = points[j]
        dx , dy = x2 - x1 , y2 - y1

        l = sqrt(dx**2 + dy**2)
        nx , ny = -dy , dx
        planes.append([nx , ny , -nx*x1 - ny*y1 - h*l])

    ans = total_area

    def dfs(points , now , nk):
        nonlocal ans
        if nk == 0 or now == n:
            ans = min(ans , cal_area(points))
            return
        if n - now > nk:
            dfs(points , now+1 , nk)
        dfs(Sutherland_Hodgman(points , *planes[now]) , now+1 , nk-1)
    dfs(points , 0 , min(n , k))

    return total_area - ans

def main():
    while True:
        try:
            n , k , h = map(int , input().split())
            if n == 0 and k == 0 and h == 0:break
            points = []
            for i in range(n):
                points.append(list(map(int , input().split())))
        except EOFError:break
        if k == 0 or h == 0:
            print("0.00")
            continue
        ans = solve(n , k , h , points)
        print(f"{ans:.2f}")

if __name__ == "__main__":
    main()

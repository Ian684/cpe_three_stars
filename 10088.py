from math import *

def generate_line(x1 , y1 , x2 , y2):
    a = y2-y1
    b = -(x2-x1)
    c = -(a*x1+b*y1)
    return [x1 , y1 , x2 , y2 , a , b , c]

def check(aimy , y1 , y2):
    if y1 < aimy <= y2 or y2 < aimy <= y1:return True
    return False

def get_x(aimy , a , b , c):
    if a == 0:
        return None
    return (-b*aimy-c)/a

def solve(n , points , maxy , miny):
    total = 0
    lines = []
    eps = 1e-9

    for i in range(n):
        j = (i + 1) % n
        x1 , y1 = points[i]
        x2 , y2 = points[j]
        lines.append(generate_line(x1 , y1 , x2 , y2))
    
    for aimy in range(maxy-1 , miny , -1):
        temp = []

        for x1 , y1 , x2 , y2 , a , b , c in lines:
            if not check(aimy , y1 , y2):continue
            aimx = get_x(aimy , a , b , c)
            if aimx is None:
                temp.append(x1)
                temp.append(x2)
            temp.append(aimx)

        temp = sorted(temp)
        for i in range(0 , len(temp) , 2):
            l = floor(temp[i])
            r = ceil(temp[i+1])
            total += r - l - 1

    return total

def main():
    while True:
        n = int(input())
        if n == 0:break
        points = []
        maxy = -1
        miny = 1 << 64
        for i in range(n):
            x , y = map(int , input().split())
            maxy = max(maxy , y)
            miny = min(miny , y)
            points.append([x , y])
        print(solve(n , points , maxy , miny))
if __name__ == "__main__":
    main()

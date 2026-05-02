from math import *

def solve(n , points):
    # A = I + B/2 - 1
    # I = A - B/2 + 1
    
    A = 0
    # 多邊面積
    B = 0
    # 線段上整數點
    
    for i in range(n):
        j = (i + 1) % n
        x1 , y1 = points[i]
        x2 , y2 = points[j]
        A += x1*y2 - x2*y1
        B += gcd(abs(x1-x2) , abs(y1-y2))
    I = (abs(A) - B + 2)/2
    # 內部整數點
    return int(I)

def main():
    while True:
        n = int(input())
        if n == 0:break
        points = []
        for i in range(n):
            x , y = map(int , input().split())
            points.append([x , y])
        print(solve(n , points))
if __name__ == "__main__":
    main()

from math import *

def distance(a , b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def compute_value(a , x , y):
    return a[0]*x+a[1]*y

def solve(rx , ry , r , x , y):
    r_angle = atan2(ry , rx)
    r1 = distance([0 , 0] , [rx , ry])
    if distance([0 , 0] , [x , y]) <= r1:return 0.000
    plus_angle = asin(r / r1)
    m1 = tan(r_angle + plus_angle)
    m2 = tan(r_angle - plus_angle)
    result1 = compute_value([m1 , -1] , x , y)
    result2 = compute_value([m2 , -1] , x , y)
    if result1*result2 > 0:
        return 0.000
    else:
        return min(compute_value([m1 , -1] , x , y)/sqrt(m1**2+1**2), compute_value([m2 , -1] , x , y)/sqrt(m2**2+1**2))

def main():
    n = int(input())
    for _ in range(n):
        rx , ry , r , x , y = map(float , input().split())
        print(f"{solve(rx , ry , r , x , y):.3f}")

if __name__ == "__main__":
    main()

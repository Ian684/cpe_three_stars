from math import *
n , radius = None , None
points = []

def distance(a , b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def isincircle(point , circle):
    if distance(point , circle[:2]) <= circle[2]:return True
    return False

def mid_point(a , b):
    return [(a[0]+b[0])/2 , (a[1]+b[1])/2]

def calculate_vertical_line(a , b):
    aa = a[::]
    bb = b[::]
    cc = [aa[0] - bb[0] , aa[1] - bb[1]]
    midx , midy = mid_point(aa , bb)
    c = -cc[0]*midx - cc[1]*midy
    return [cc[0] , cc[1] , c]

def compute_three_points(a , b , c):
    first_line = calculate_vertical_line(a , b)
    second_line = calculate_vertical_line(a , c)
    if first_line[0] == second_line[0] and first_line[1] == second_line[1]:
        d , x , y = sorted([[distance(a , b) , a , b] , [distance(a , c) , a , c] , [distance(b , c) , b , c]])[2]
        x , y = mid_point(x , y)
        return [x , y , d]
    if first_line[0] == 0:
        first_line = calculate_vertical_line(b , c)
    if second_line[0] == 0:
        second_line = calculate_vertical_line(b , c)
    multiply = second_line[0] / first_line[0]
    first_line = [0 , second_line[1] - first_line[1]*multiply , second_line[2] - first_line[2]*multiply]
    y = -(first_line[2]/first_line[1])
    x = -((second_line[1]*y+second_line[2])/second_line[0])
    return [x , y , distance([x , y] , a)]

def valid(circle):
    global radius
    return circle[2] <= radius

def solve():
    global n , points , radius
    circle = [1 << 60 , 1 << 60 , -1]
    for i in range(n):
        if isincircle(points[i] , circle):continue
        circle = points[i]+[0]
        for j in range(i):
            if isincircle(points[j] , circle):continue
            circle = mid_point(points[i] , points[j])+[distance(points[i] , points[j])/2]
            if not valid(circle):return False
            for k in range(j):
                if isincircle(points[k] , circle):continue
                circle = compute_three_points(points[i] , points[j] , points[k])
                if not valid(circle):return False
    return True
def main():
    global n , points , radius 
    while True:
        n = int(input())
        if n == 0:break
        points = []
        for i in range(n):
            points.append(list(map(int , input().split())))
        radius = float(input())
        if solve():
            print("The polygon can be packed in the circle.")
        else:
            print("There is no way of packing that polygon.")
if __name__ == "__main__":
    main()

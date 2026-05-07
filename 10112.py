from math import *

def cal_area(a , b , c):
    return abs(0.5*((c[1]-a[1])*(b[0]-a[0])-(b[1]-a[1])*(c[0]-a[0])))

def check(n , points , i , j , k):
    a , b , c = points[i] , points[j] , points[k]
    aim_area = cal_area(a , b , c)
    for p in range(n):
        if p == i or p == j or p == k:continue
        _next = points[p]
        total_area = cal_area(a , b , _next) + cal_area(a , _next , c) + cal_area(_next , b , c)
        if total_area == aim_area:return None

    return aim_area

def solve(n , points):

    ans = [-1 , '' , '' , '']
    
    for i in range(n):
        for j in range(i+1 , n):
            for k in range(j+1 , n):
                result = check(n , points , i , j , k)
                if result is None:continue
                if result > ans[0]:
                    ans = [result , i , j , k]
    return ans

def main():
    while True:
        n = int(input())
        if n == 0:break
        points = []
        labels = []
        for i in range(n):
            label , x , y = input().split()
            labels.append(label)
            points.append([int(x) , int(y)])
        ans = solve(n , points)
        print(labels[ans[1]] , end="")
        print(labels[ans[2]] , end="")
        print(labels[ans[3]] , end="")
        print()

if __name__ == "__main__":
    main()

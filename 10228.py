from math import *
from random import random

def get_dist_sum(start , points):
    count = 0
    x , y = start
    for dx , dy in points:
        count += sqrt((x - dx)**2 + (y - dy)**2)
    return count

def solve(points):
    n = len(points)
    start = [0 , 0]
    for x , y in points:
        start[0] += x
        start[1] += y
    start[0] /= n
    start[1] /= n
    temp = 10000
    min_dist = get_dist_sum(start , points)
    cur_dist = min_dist
    delta = 0.999
    
    while True:
        if temp <= 1e-4:break
        nx = start[0] + (random() * 2 - 1) * temp
        ny = start[1] + (random() * 2 - 1) * temp
        new_dist = get_dist_sum([nx , ny] , points)
        if new_dist < cur_dist:
            start = [nx , ny]
            cur_dist = new_dist
        elif random() < exp((cur_dist - new_dist) / temp):
            start = [nx , ny]
            cur_dist = new_dist
        min_dist = min(min_dist , new_dist)
        temp *= delta
    return int(min_dist+0.5)

def main():
    t = int(input())
    for _ in range(t):
        blank_line = input()
        n = int(input())
        points = []
        for i in range(n):
            x , y = map(int , input().split())
            points.append([x , y])
        ans = solve(points)
        print(ans)
        if _ != t - 1:
            print()

if __name__ == "__main__":
    main()

from math import *

def generate_lines(points):
    lines = []
    for j in range(len(points)):
        k = (j+1)%len(points)
        mx , my = points[j]
        lx , ly = points[k]
        a = (ly - my)
        if a == 0:continue
        b = -(lx - mx)
        c = -(a*mx + b*my)
        lines.append([a , b , c , lx , ly , mx , my])
    return lines

def get_x_set(ny , lines):
    x_set = []
    for a , b , c , lx , ly , mx , my in lines:
        if min(my , ly) <= ny <= max(my , ly):
            x_set.append((-b*ny-c)/a)
    return sorted(x_set)

def main():
    c = int(input())
    blank_line = input()
    for _ in range(c):
        points = []
        bi = -1
        sm = 1 << 60
        while True:
            try:
                line = input()
                if line == "":break
                a , b = map(int , line.split())
                bi = max(bi , b)
                sm = min(sm , b)
                points.append([a , b])
            except EOFError:break
        ans = 0
        eps = 1e-7
        lines = generate_lines(points)
        for ny in range(bi-1 , sm-1 , -1):
            lastx = get_x_set(ny+1-eps , lines)
            nowx = get_x_set(ny+eps , lines)
            for i in range(0 , len(lastx) , 2):
                for j in range(0 , len(nowx) , 2):
                    l = ceil(max(lastx[i] , nowx[j]))
                    r = floor(min(lastx[i+1] , nowx[j+1]))
                    if r <= l:continue
                    ans += r - l
        print(ans)
        if _ != c-1:print()
if __name__ == "__main__":
    main()

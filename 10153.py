from math import *

def dis(a , b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def solve(mx , my , mz , x , y , z , r):

    o1 = (-mx)*(x-mx)+(-my)*(y-my)+(-mz)*(z-mz)
    o2 = (-x)*(mx-x)+(-y)*(my-y)+(-z)*(mz-z)

    if o1 < 0 or o2 < 0:
        return True
    angle = ((-mx)*(x-mx)+(-my)*(y-my)+(-mz)*(z-mz))/(dis([0 , 0 , 0] , [mx , my , mz])*dis([x , y , z] , [mx , my , mz]))
    angle = acos(max(-1 , min(1 , angle)))
    l1 = sin(angle)*dis([0 , 0 , 0] , [mx , my , mz])
    if l1 - r > 0:
        return True
    return False

def main():
    while True:
        try:
            r = float(input())/2
            main_h , main_a , main_b = map(float , input().split())
            main_a = main_a/180*pi
            main_b = main_b/180*pi
            main_h += r
            mz = main_h*sin(main_a)
            main_h = main_h*cos(main_a)
            my = main_h*sin(main_b)
            mx = main_h*cos(main_b)
            n = int(input())
            ans = []
            for i in range(n):
                line = input().split()
                h , a , b = float(line[0]) , float(line[1]) , float(line[2])
                h += r
                name = ' '.join(line[3:])
                a = a/180*pi
                b = b/180*pi
                z = h*sin(a)
                h = h*cos(a)
                y = h*sin(b)
                x = h*cos(b)
                if solve(mx , my , mz , x , y , z , r):
                    ans.append(name)
            ans = sorted(ans)
            for i in range(len(ans)):
                print(ans[i])
            print()
        except EOFError:break

if __name__ == "__main__":
    main()

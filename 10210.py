from math import *

def main():
    while True:
        try:
            x1 , y1 , x2 , y2 , cmd , enf = map(float , input().split())
        except EOFError:break
        cmd = cmd/180*pi
        enf = enf/180*pi
        ab = sqrt((x1-x2)**2+(y1-y2)**2)
        a = ab/sin(enf)
        b = ab/sin(cmd)
        ans = a*cos(enf)+b*cos(cmd)
        print(f"{ans:.3f}")

if __name__ == "__main__":
    main()

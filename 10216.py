from math import *

def main():
    t = int(input())
    for _ in range(t):
        a , b , c = sorted(list(map(int , input().split())))
        if a + b < c:
            dm , di , dg = 1 , 1 , 1
            do = 1
        else:
            mx = 120/180*pi
            s = (a + b + c) / 2
            area = sqrt(s*(s-a)*(s-b)*(s-c))
            if acos((a**2+b**2-c**2)/(2*a*b)) < mx:
                dm = sqrt((a**2+b**2+c**2+4*sqrt(3)*area)/2)
            else:
                dm = a + b
            i = (2*area)/(a + b + c)
            n = (a + b - c) / 2
            di = sqrt((n)**2+i**2) + sqrt((a-n)**2+i**2) + sqrt((b-n)**2+i**2)
            cosA = (b**2+c**2-a**2)/(2*b*c)
            cosB = (a**2+c**2-b**2)/(2*a*c)
            x1 = sqrt(c**2+(b/2)**2-b*c*cosA)
            x2 = sqrt((c/2)**2+b**2-b*c*cosA)
            x3 = sqrt(c**2+(a/2)**2-a*c*cosB)
            dg = (2/3)*(x1+x2+x3)
            if a + b == c:
                do = -1
            else:
                do = (3*a)/(2*sin(acos((b**2+c**2-a**2)/(2*b*c))))

        print(f"{dm:.3f} {di:.3f} {dg:.3f} {do:.3f}")

if __name__ == "__main__":
    main()

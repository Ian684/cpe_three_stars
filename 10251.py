from math import *

def main():
    n = int(input())
    for i in range(n):
        line = list(map(int , input().split()))
        if len(line) == 3:
            R , h , r = line
            cita = acos(r/R)
            ans = R**2*cita - sin(cita)*R*r
        else:
            l , h , x , y = line
            m = l/2
            if x == 0 or y == 0:
                ans = l*(m - max(x , y))
            else:
                rx , ry = -y , x
                x1 = ((m - y) / ry) * rx + x
                y1 = ((m - x) / rx) * ry + y
                x1 = m - x1
                y1 = m - y1
                ans = x1 * y1 / 2
        print(f"{ans*h:.3f}")
    
if __name__ == "__main__":
    main()

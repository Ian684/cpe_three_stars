from math import *

def main():
    while True:
        v , n = map(int , input().split())
        if v == 0 and n == 0:break
        x , y , r = map(float , input().split())
        x , y , r = round(x*100), round(y*100), r / 180 * pi
        ps = []
        for i in range(v):
            a , b = map(float , input().split())
            a, b = round(a*100), round(b*100)
            ps.append([a , b])
        lines = []
        for i in range(v):
            j = (i + 1) % v
            a1 , b1 = ps[i]
            a2 , b2 = ps[j]
            r1 = atan2(b2 - b1 , a2 - a1)
            if a2 - a1 == 0:
                lines.append([r1 , a1 , b1 , a2 , b2 , 1 , 0 , -a1])
                continue
            lines.append([r1 , a1 , b1 , a2 , b2 , (b2-b1)/(a2-a1) , -1 , -(b2-b1)/(a2-a1)*a1+b1])

        flag = True
        eps = 1
        for _ in range(n+1):

            for i , j in ps:
                if round(x) == i and round(y) == j:
                    flag = False
                    break
            if not flag:break

            temp = []

            for i in range(len(lines)):
                r1, a1, b1, a2, b2, a, b, c = lines[i]

                d = x*a + y*b + c
                den = a*cos(r) + b*sin(r)

                if abs(den) < 1e-10:
                    continue

                k = -d / den

                if k <= 1e-9:
                    continue

                dx = x + k*cos(r)
                dy = y + k*sin(r)

                if (min(a1, a2) - 1e-8 <= dx <= max(a1, a2) + 1e-8
                    and min(b1, b2) - 1e-8 <= dy <= max(b1, b2) + 1e-8):
                    temp.append((k, r1))

            if not temp:
                flag = False
                break

            k, r1 = min(temp)

            x = x + k*cos(r)
            y = y + k*sin(r)

            r = (2*r1 - r) % (2*pi)

        for i , j in ps:
            if round(x) == i and round(y) == j:
                flag = False
                break
        if flag:
            print(f"{x/100:.2f} {y/100:.2f}")
        else:
            print("lost forever...")

if __name__ == "__main__":
    main()

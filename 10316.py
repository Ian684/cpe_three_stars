from math import *

def change_to_xyz(a , b):

    a = a / 180 * pi
    b = b / 180 * pi
    z = sin(a)
    y = cos(a)*sin(b)
    x = cos(a)*cos(b)

    return x , y , z

def main():
    eps = 1e-10
    while True:
        try:
            n = int(input())
            ps = []
            temp = []
            for i in range(n):
                a , b = map(float , input().split())
                temp.append([a , b])
                x , y , z = change_to_xyz(a , b)
                ps.append([x , y , z])
        except EOFError:break

        mn = 1 << 32
        ans = None
        for i in range(n):
            x , y , z = ps[i]
            now = 0
            for j in range(n):
                if i == j:continue
                nx , ny , nz = ps[j]

                now = max(now , (nx-x)**2 + (ny-y)**2 + (nz-z)**2)
            if now < mn - eps:
                mn = now
                ans = temp[i]
            elif abs(now - mn) <= eps:
                ans = temp[i]
        print(f"{ans[0]:.2f} {ans[1]:.2f}")

if __name__ == "__main__":
    main()

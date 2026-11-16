from math import *

def main():
    while True:
        try:
            l , w , r = map(float , input().split())
        except EOFError:break

        ans = (3/4)*pi*(r**2) + (1/4)*pi*(max(0 , r - w)**2) + (1/4)*pi*(max(0 , r - l)**2)
        if r > l + w:
            r1 = r - w
            r2 = r - l
            d = sqrt(l**2 + w**2)

            a = acos((d**2 + r1**2 - r2**2) / (2*d*r1))
            b = acos((d**2 + r2**2 - r1**2) / (2*d*r2))

            s3 = (1/2)*d*r1*sin(a) - (1/2)*l*w
            a = a - atan2(w , l)
            b = b - atan2(l , w)

            s1 = r1**2 * a * (1/2)
            s2 = r2**2 * b * (1/2)

            ans -= s1 + s2 - s3
        print(f"{ans:.10f}")

if __name__ == "__main__":
    main()

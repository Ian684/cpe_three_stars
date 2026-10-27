from math import isqrt

def pell(d):
    a0 = isqrt(d)
    m, den, a = 0, 1, a0
    p0, p = 1, a
    q0, q = 0, 1

    while p * p - d * q * q != 1:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den

        p0, p = p, a * p + p0
        q0, q = q, a * q + q0

    return p, q

def main():
    limit = 16 * 10**34
    ans = set()

    for k in range(1, 16, 2):
        g, r = (1, 3) if k == 9 else (k, 1)
        d = 8 * g

        a, b = pell(d)
        x, y = a, b

        while (g * r * y) ** 2 < limit:
            ans.add((g * r * y) ** 2)
            x, y = a * x + d * b * y, b * x + a * y

    for v in sorted(ans):
        print(v)

if __name__ == "__main__":
    main()

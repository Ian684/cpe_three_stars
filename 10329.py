from math import *
import sys

def main():

    limit = int(sqrt(5010)) + 1
    seive = [True] * limit
    seive[0] = seive[1] = False

    for i in range(2, isqrt(limit) + 1):
        if seive[i]:
            for j in range(i*i, limit, i):
                seive[j] = False

    prime = [k for k, v in enumerate(seive) if v]

    C = [{} for _ in range(5001)]

    for i in range(2, 5001):
        temp = C[i-1].copy()
        aim = i

        for p in prime:
            if p*p > aim:
                break

            if aim % p == 0:
                count = 0
                while aim % p == 0:
                    aim //= p
                    count += 1

                temp[p] = temp.get(p, 0) + count

        if aim > 1:
            temp[aim] = temp.get(aim, 0) + 1

        C[i] = temp

    data = iter(map(int, sys.stdin.read().split()))

    for n in data:
        m = next(data)
        factor = {}

        for i in range(n + m):
            a, b = next(data), next(data)
            sign = 1 if i < n else -1

            factor[a] = factor.get(a, 0) + sign
            factor[b] = factor.get(b, 0) - sign
            factor[a-b] = factor.get(a-b, 0) - sign

        exp = {}

        for k, v in factor.items():
            if v == 0:
                continue

            for p, count in C[k].items():
                exp[p] = exp.get(p, 0) + count*v

        if any(v < 0 for v in exp.values()):
            print(0)
            continue

        result = 1

        for p, count in exp.items():
            if count >= 333:
                result = -1
                break

            result *= p**count

            if result >= 10**100:
                result = -1
                break

        print(result)

if __name__ == "__main__":
    main()

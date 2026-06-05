from math import *

def main():
    limit = int(sqrt(10**9))+100
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit))+1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False
    
    prime = []
    for k , v in enumerate(seive):
        if v:
            prime.append(k)

    while True:
        n = int(input())
        if n == 0:break
        ans = n
        for p in prime:
            if n <= 1:break
            if n % p == 0:
                ans *= ((p-1)/p)
                while n % p == 0:
                    n //= p
        if n != 1:
            ans *= ((n-1)/n)
        print(int(ans))

if __name__ == "__main__":
    main()

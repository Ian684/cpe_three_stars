from math import *

def get_prime():

    limit = int(sqrt(2000)) + 1
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False

    prime = []
    for k , v in enumerate(seive):
        if v:
            prime.append(k)
    
    return prime

def phi(aim):

    temp = aim
    result = aim
    for p in prime:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result //= p
            result *= (p - 1)
    if temp > 1:
        result //= temp
        result *= (temp - 1)
    return result

prime = get_prime()
def main():
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:break
        N = (2*a+1)*(2*b+1)-1
        K = 0
        for x in range(1 , a+1):
            k = b // x
            K += phi(x)*k
            for y in range(k*x+1 , b+1):
                if gcd(x , y) == 1:
                    K += 1
        K = 4*K+4
        print(f"{K/N:.7f}")

if __name__ == "__main__":
    main()

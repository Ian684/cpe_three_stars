from math import *

def generate_prime():
    limit = int(sqrt(2**31))+100
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

    return prime

def get_legendre_count(n , p):
    count = 0
    while n > 0:
        count += n // p
        n //= p
    return count


def main():
    prime = generate_prime()
    while True:
        try:
            fac , aim = map(int , input().split())
        except EOFError:break
        if aim == 0:
            print(f"{aim} does not divide {fac}!")
            continue
        if aim == 1:
            print(f"{aim} divides {fac}!")
            continue
        original_aim = aim
        i = 0
        valid = True
        while aim > 1 and i < len(prime):
            if aim % prime[i] == 0:
                count = 0
                while aim % prime[i] == 0:
                    count += 1
                    aim //= prime[i]
                if count > 0 and not (get_legendre_count(fac , prime[i]) >= count):
                    valid = False
                    break
            i += 1
        if valid and aim > 1:
            if not (fac >= aim):
                valid = False
        if valid:
            print(f"{original_aim} divides {fac}!")
        else:
            print(f"{original_aim} does not divide {fac}!")

if __name__ == "__main__":
    main()

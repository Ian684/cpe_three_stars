from math import *

def main():
    while True:
        try:
            n = int(input())
        except EOFError:break
        if n == 1:
            print(1)
            continue
        if n == 2:
            print(3)
            continue
        ans1 , ans2 = 0 , 1
        for i in range(n):
            a , b = 1 , n - i
            l = lcm(ans2 , b)
            ans1 = (l // ans2) * ans1 + (l // b) * a
            ans2 = l
            g = gcd(ans1 , ans2)
            ans1 //= g
            ans2 //= g
        ans1 *= n
        g = gcd(ans1 , ans2)
        ans1 //= g
        ans2 //= g
        a = str(ans1 // ans2)
        b = str(ans1 % ans2)
        c = str(ans2)
        print(f"{' '*len(a)+' '+b}")
        print(f"{a+' '+'-'*len(c)}")
        print(f"{' '*len(a)+' '+c}")

if __name__ == "__main__":
    main()

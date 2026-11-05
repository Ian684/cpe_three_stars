from math import *

def main():
    while True:
        p , q = map(int , input().split())
        if p == 0 and q == 0:break
        if p == 0:
            print(0 , 2)
            continue
        if p == q:
            print(2 , 0)
            continue
        flag = False
        for total in range(2 , 50001):
            if p*total*(total-1) % q:continue
            k = (p*total*(total-1)) // q
            d = (1+sqrt(1 + 4*k))/2
            if int(d) == d:
                flag = True
                print(int(d) , total-int(d))
                break
        if not flag:
            print("impossible")

if __name__ == "__main__":
    main()

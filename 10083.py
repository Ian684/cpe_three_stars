from math import *

def main():
    while True:
        try:
            t , a , b = map(int , input().split())
        except EOFError:break
        flag = True
        if t == 1:
            flag = False
        if a % b != 0:
            flag = False
        if flag and (a-b)*log(t , 10) >= 100:
            flag = False
        if flag and a == b:
            ans = 1
        if flag and a != b:
            val_a = (t**a - 1)
            val_b = (t**b - 1)
            ans = val_a // val_b
        if flag:
            print(f"({t}^{a}-1)/({t}^{b}-1) {ans}")
        else:
            print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")
if __name__ == "__main__":
    main()

from math import *

def main():
    while True:
        try:
            n = int(input())
        except EOFError:break
        k = (sqrt(4*n+1)-1)/2
        print(f"{k:.2f} {ceil(k+1e-9)}")

if __name__ == "__main__":
    main()

# 前k-1都不中獎
# p(1) = 1
# p(2) = p(1)*(n-(k-1))/n
# p(k) = (n-1)*(n-2)...(n-(k-1))/n**(k-1)
# 第k個中獎且前面都不中獎 => f(k) = p(k)*k/n
# 當 f(k+1)/f(k) <= 1 時，f(k)達到頂峰，
# f(k+1)/f(k) = (k+1)*(n-k)/(n*k) <= 1
# k = (sqrt(4*n+1)-1)/2

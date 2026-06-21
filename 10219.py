from math import *

def main():
    while True:
        try:
            n , k = map(int , input().split())
        except EOFError:break
        count = 0
        for i in range(n , max(n-k , k) , -1):
            count += log(i , 10)
        for i in range(min(n-k , k) , 1 , -1):
            count -= log(i , 10)
        print(int(count)+1)

if __name__ == "__main__":
    main()

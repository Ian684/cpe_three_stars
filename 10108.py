from math import *

def formula(n):
    if n & 1:
        return (n+1)//2*n
    return n//2*(n+1)

def main():
    while True:
        n , day = map(int , input().split())
        if n < 0 or day < 0:break
        for d in range(1 , day+1):
            if d % 7 == 0:
                n = isqrt(n)
            else:
                n = formula(n)
            if n == 1 or n == 0:break
        
        day = str(day)
        if day == '11' or day == '12' or day == '13':
            day += "'th"  
        elif day[-1] == '1':
            day += "'st"
        elif day[-1] == '2':
            day += "'nd"
        elif day[-1] == '3':
            day += "'rd"
        else:
            day += "'th"
        print(f"Number of mosquitos in the pond at the end of {day} day is {n}.")

if __name__ == "__main__":
    main()

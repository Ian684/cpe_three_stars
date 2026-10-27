from math import *

def main():
    x = [0 , 1 , 2]
    now = 2
    i = 3
    while i < 10010:
        x.append(x[i-1]+now)
        i += 1
        x.append(x[i-1]+now)
        i += 1
        now += 1
    while True:
        try:
            n , dist , d = map(int , input().split())
        except EOFError:break
        cita = 2*asin(dist/(2*d))
        l = d*cita
        total = 0
        if x[n] & 1:
            total += dist
        total += (dist+l)*(x[n]//2)
        print(x[n] , round(total))

if __name__ == "__main__":
    main()

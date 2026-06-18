def get2(aim):
    if not aim:
        return 0
    return aim//2 + get2(aim//2)

def get5(aim):
    if not aim:return 0
    return aim//5 + get5(aim//5)

def getodd(aim , base):
    if not aim:return 0
    flag = 0
    if aim % 10 >= base:flag = 1
    return aim//10 + flag + getodd(aim//5 , base)

def geteven(aim , base):
    if not aim:return 0
    return geteven(aim//2 , base) + getodd(aim , base)

def main():
    recursive = {2:[6 , 2 , 4 , 8] , 3:[1 , 3 , 9 , 7] , 7:[1 , 7 , 9 , 3] , 9:[1 , 9 , 1 , 9]}
    while True:
        try:
            n , m = map(int , input().split())
        except EOFError:break
        m = n - m
        n2 , n5 = get2(n) - get2(m) , get5(n) - get5(m)
        if n5 > n2:
            print(5)
            continue
        else:
            n2 -= n5 
            n5 = 0
        n3 = geteven(n , 3) - geteven(m , 3)
        n7 = geteven(n , 7) - geteven(m , 7)
        n9 = geteven(n , 9) - geteven(m , 9)
        ans = 1
        if n2:
            ans *= recursive[2][n2%4]
        ans *= recursive[3][n3%4] * recursive[7][n7%4] * recursive[9][n9%4]
        ans %= 10
        print(ans)

if __name__ == "__main__":
    main()

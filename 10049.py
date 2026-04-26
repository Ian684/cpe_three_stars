def main():
    g = [0]*700000
    g[1] = 1
    g[2] = 3
    m = 0
    for k in range(2 , len(g)):
        while g[m] < k:
            m += 1
        g[k] = g[k-1]+m
    while True:
        n = int(input())
        if n == 0:break
        l , r = 0 , len(g)-1
        flag = False
        while True:
            if l >= r:break
            mid = (l + r)//2
            if n > g[mid]:
                l = mid+1
            elif n <= g[mid]:
                r = mid
        print(r)
if __name__ == "__main__":
    main()

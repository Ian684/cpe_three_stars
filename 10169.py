def main():
    limit = 10**6+10
    w1 , w2 = 0 , 1
    check = [[0 , 0]]
    s = 1
    s1 = 1
    c = 0
    for i in range(limit):
        temp = 1 / ((w1+1) * (w2+1))
        s1 *= temp
        s *= (1-temp)
        w1 += 1
        w2 += 1
        t = str(s1)
        if 'e' in t:
            ct = int(t.split('-')[-1])-1
        else:
            ct = 0
            for j in t.split('.')[-1]:
                if j != '0':break
                ct += 1
        s1 *= 10**ct
        c += ct
        check.append([1-s , c])

    while True:
        try:
            n = int(input())
            print(f"{check[n][0]:.6f} {check[n][1]}")
        except EOFError:break
        
if __name__ == "__main__":
    main()

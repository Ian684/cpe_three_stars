def main():
    f = [1 , 2]
    for i in range(2 , 900):
        temp = f[i-1]+f[i-2]
        f.append(temp)
        i += 1
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:break
        c = 0
        for i in range(len(f)):
            if f[i] > b:break
            if f[i] < a:continue
            c += 1
        print(c)

if __name__ == "__main__":
    main()

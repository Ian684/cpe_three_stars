def main():
    fac = [0 , 1]
    for i in range(2 , 2010):
        fac.append(fac[i-1]*i)
    while True:
        try:
            n = int(input())
        except EOFError:break
        print(fac[2*n]//fac[n]//fac[n+1])

if __name__ == "__main__":
    main()

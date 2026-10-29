def main():
    C = [0 , 1]
    for i in range(2 , 100):
        C.append(C[-1]*i)
    while True:
        try:
            k , d = map(int , input().split())
        except EOFError:break
        ans = 1
        total = (1-k**(d+1))//(1-k) - 1
        for i in range(d):
            ans *= (C[total]/C[total//k]/C[total-total//k])
            total //= k
            total -= 1
        print(ans)

if __name__ == "__main__":
    main()

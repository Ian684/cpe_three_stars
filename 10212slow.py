def main():
    while True:
        try:
            n , m = map(int , input().split())
        except EOFError:break
        m = n - m + 1
        count = {2:0 , 5:0}
        ans = 1
        for i in range(n , m-1 , -1):
            temp = i
            for p in [2 , 5]:
                if temp % p == 0:
                    while temp % p == 0:
                        count[p] += 1
                        temp //= p
                    if temp <= 1:break
            temp %= 10
            ans *= temp
            ans %= 10
        zero = min(count[2] , count[5])
        count[2] -= zero
        count[5] -= zero
        for p in [2 , 5]:
            if count[p] == 0:continue
            for i in range(count[p]):
                ans *= p
                ans %= 10
        print(ans)

if __name__ == "__main__":
    main()

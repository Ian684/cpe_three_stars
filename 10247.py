# import sys
# sys.set_int_max_str_digits(0)

def main():
    C = [1 , 1]
    for i in range(2 , 3280):
        C.append(C[-1]*i)
    while True:
        try:
            k , d = map(int , input().split())
        except EOFError:break
        if k == 1:
            print(1)
            continue
        ans = 1
        now = 1
        total = (1 - k**(d+1)) // (1 - k) - 1
        for i in range(d):
            temp = 1
            aim = total // k
            for j in range(k-1):
                temp *= C[total]//C[aim]//C[total-aim]
                total -= aim
            total = aim - 1
            ans *= temp**now
            now *= k
        print(ans)

if __name__ == "__main__":
    main()

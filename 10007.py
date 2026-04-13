def main():
    factorial = {1:1}
    for i in range(2 , 301):
        factorial[i] = factorial[i-1]*i
    catalan = {1:1}
    for i in range(2 , 301):
        catalan[i] = catalan[i-1]*(4*i-6)//i
    while True:
        n = int(input())
        if n == 0:break
        print(factorial[n]*catalan[n+1])
if __name__ == "__main__":
    main()

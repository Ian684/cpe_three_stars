def generate():
    factorial = [1]*14
    for i in range(1 , 14):
        factorial[i] = i*factorial[i-1]
    return factorial

def main():
    
    factorial = generate()
    while True:
        try:
            n , k = map(int , input().split())
            ns = list(map(int , input().split()))
        except EOFError:break
        result = 1
        for nn in ns:
            temp = 1
            temp *= (factorial[n]/(factorial[nn]*factorial[n-nn]))
            n -= nn
            result *= temp
        print(int(result))
if __name__ == "__main__":
    main()

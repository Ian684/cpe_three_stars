def generate():
    check = {}
    for i in range(1 , 21):
        c = 1
        for j in range(i , 0 , -1):
            c *= j
        check[i] = c
    return check
def main():
    check = generate()
    c = int(input())
    for i in range(c):
        s = input()
        arr = []
        for k in s:
            arr.append(k)
        n = int(input())
        arr = sorted(arr)
        l = len(s)
        for k in range(l-1 , 0 , -1):
            a = (n // check[k])
            n %= check[k]
            print(arr[a] , end="")
            del arr[a]
        print(arr[0])
if __name__ == "__main__":
    main()

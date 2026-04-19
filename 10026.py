import sys

def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    c = int(next(tokens))
    for cc in range(c):
        n = int(next(tokens))
        arr = []
        for q in range(n):
            t = int(next(tokens))
            s = int(next(tokens))
            arr.append([t , s , q+1])
        arr = sorted(arr , key=lambda x:(x[0]/x[1] , x[2]))
        for i in range(n-1):
            print(arr[i][2] , end=" ")
        print(arr[-1][2])
        if cc != c-1:print()
if __name__ == "__main__":
    main()

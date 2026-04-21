# bridge problem zero judge  
def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                print(0)
                continue
            arr = list(map(int , input().split()))
        except EOFError:break
        arr = sorted(arr)
        r = n-1
        ans = 0
        while True:
            if r == 2:
                ans += arr[1] + arr[0] + arr[2]
                break
            elif r == 1:
                ans += arr[1]
                break
            elif r == 0:
                ans += arr[0]
                break
            else:
                ans += min(arr[1]+arr[0]+arr[r]+arr[1] , arr[r]+arr[0]+arr[r-1]+arr[0])
            r -= 2
        print(ans)
if __name__ == "__main__":
    main()

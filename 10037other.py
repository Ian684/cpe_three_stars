# bridge problem uva online judge
def main():
    c = int(input())
    for cc in range(c):
        blank_line = input()
        n = int(input())
        if n == 0:
            print(0)
            continue
        arr = sorted([int(input()) for _ in range(n)])
        r = n-1
        ans = 0
        result = []
        while True:
            if r == 2:
                ans += arr[1] + arr[0] + arr[2]
                result.append([arr[0] , arr[1]])
                result.append([arr[0]])
                result.append([arr[0] , arr[2]])
                break
            elif r == 1:
                ans += arr[1]
                result.append([arr[0] , arr[1]])
                break
            elif r == 0:
                ans += arr[0]
                result.append([arr[0]])
                break
            else:
                x = arr[1]+arr[0]+arr[r]+arr[1]
                y = arr[r]+arr[0]+arr[r-1]+arr[0]
                if x > y:
                    ans += y
                    result.append([arr[0] , arr[r-1]])
                    result.append([arr[0]])
                    result.append([arr[0] , arr[r]])
                    result.append([arr[0]])
                else:
                    ans += x
                    result.append([arr[0] , arr[1]])
                    result.append([arr[0]])
                    result.append([arr[r-1] , arr[r]])
                    result.append([arr[1]])
            r -= 2
        print(ans)
        for a in result:
            print(' '.join(map(str , a)))
        if cc != c-1:print()
if __name__ == "__main__":
    main()

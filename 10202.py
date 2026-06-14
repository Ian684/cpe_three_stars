def main():
    while True:
        try:
            line = list(map(int , input().split()))
            n = line[0]
            arr = line[1:]
        except EOFError:break
        arr = sorted(arr)
        valid = False
        best = [1 << 60]
        for i in range(2 , len(arr)):
            check = set()
            check.add(0)
            check.add(1)
            ans = []
            temp = arr[0] + arr[1] - arr[i]
            if temp & 1:
                continue
            ans.append(temp // 2)
            ans.append(arr[0] - ans[0])
            ans.append(arr[1] - ans[0])
            if ans[1] + ans[2] != arr[i]:
                continue
            check.add(i)
            start = 0
            while len(ans) < n:
                aim = -1
                u = -1
                for j in range(start , len(arr)):
                    if j in check:continue
                    aim = arr[j]
                    u = j
                    break
                check.add(u)
                ans.append(aim - ans[0])
                start = u + 1
                for k in range(1 , len(ans)-1):
                    aim = ans[-1] + ans[k]
                    for j in range(start , len(arr)):
                        if j in check:continue
                        if arr[j] == aim:
                            check.add(j)
                            break
            if len(check) == len(arr):
                valid = True
                if ans < best:
                    best = ans[::]
                
        if valid:
            print(' '.join(map(str , best)))
        else:
            print("Impossible")


if __name__ == "__main__":
    main()

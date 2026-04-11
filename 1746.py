def main():
    while True:
        try:
            n = int(input())
            arr = list(map(int , input().split()))
        except EOFError:break
        if sum(arr) & 1:
            print("no quotation")
            continue
        trr = []
        flag = False
        for kk in range(min(arr[0] , arr[-1]) , 0 , -1):
            i , j = 0 , n-1
            trr = arr[::]
            k = kk
            while i < n and j >= 0 and k > 0 and trr[i] >= k and trr[j] >= k:
                trr[i] -= k
                trr[j] -= k
                if trr[i] == 0:
                    i += 1
                if trr[j] == 0:
                    j -= 1
                k -= 1
            if k == 0 and kk != 1:
                flag = True
                break
            if k == 0 and kk == 1:
                if sum(arr) == 2:
                    flag = True
                break
        if not flag:
            print("no quotation")
        else:
            print(kk)
if __name__ == "__main__":
    main()

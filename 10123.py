def valid(arr , check , l , w , n):
    total = w*1.5
    for i in range(n):
        if check[i]:continue
        total += arr[i][1]*(arr[i][0]+1.5)
    
    if total < 0:
        return False

    total = w*-1.5
    for i in range(n):
        if check[i]:continue
        total += arr[i][1]*(arr[i][0]-1.5)

    if total > 0:
        return False

    return True

def main():
    now = 0
    while True:
        l , w , n = map(int , input().split())
        if l == 0 and w == 0 and n == 0:break

        arr = []
        for i in range(n):
            pos , weight = map(int , input().split())
            arr.append([pos , weight])
        print(f"Case {now+1}:")
        now += 1
        check = [False]*n
        if not valid(arr , check , l , w , n):
            print("Impossible")
            continue

        ans = []

        def dfs(count):
            nonlocal l , w , n , arr , ans , check
            if count >= n:
                return True
            
            for i in range(n):
                if check[i]:continue
                check[i] = True
                if valid(arr , check , l , w , n):
                    if dfs(count + 1):
                        ans.append(i)
                        return True
                check[i] = False
            return False

        if not dfs(0):
            print("Impossible")
            continue
        for i in ans[::-1]:
            a , b = arr[i]
            print(a , b)

if __name__ == "__main__":
    main()

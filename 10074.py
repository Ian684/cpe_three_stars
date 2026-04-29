def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        arr = []
        for i in range(n):
            arr.append(list(map(int , input().split())))
        height = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    if i == 0:
                        height[i][j] = 1
                    else:
                        height[i][j] = height[i-1][j] + 1
        ans = 0

        for i in range(n):
            for j in range(m):

                if arr[i][j] == 1:continue

                min_h = height[i][j]
                for k in range(j , -1 , -1):
                    
                    if arr[i][j] == 1:break

                    min_h = min(min_h , height[i][k])
                    width = j - k + 1
                    ans = max(ans , min_h * width)
        print(ans)

if __name__ == "__main__":
    main()

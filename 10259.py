memory = []
directions = ((-1,0),(1,0),(0,-1),(0,1))

def dfs(n , k , arr , x , y):
    global memory , directions

    if memory[x][y] != -1:return memory[x][y]
    count = 0
    for i in range(1 , k+1):
        for dx , dy in directions:
            nx , ny = x + dx*i , y + dy*i
            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if arr[nx][ny] <= arr[x][y]:continue
            count = max(count , dfs(n , k , arr , nx , ny))

    memory[x][y] = count + arr[x][y]
    return memory[x][y]            

def main():
    global memory 
    test = int(input())
    for case in range(test):
        line = input()
        n , k = map(int , input().split())
        arr = []
        for i in range(n):
            arr.append(list(map(int , input().split())))
        memory = [[-1]*n for _ in range(n)]
        ans = dfs(n , k , arr , 0 , 0)
        print(ans)
        if case != test - 1:print()

if __name__ == "__main__":
    main()

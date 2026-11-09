def solve(n , m , arr):


    directions = ((-1,0),(1,0),(0,-1),(0,1))
    memory = [[-1]*m for _ in range(n)]
    
    def dfs(i , j):

        nonlocal directions , memory 
        if memory[i][j] != -1:
            return memory[i][j]


        result = 0
        for dx , dy in directions:
            nx , ny = i + dx , j + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if arr[nx][ny] < arr[i][j]:
                result = max(result , dfs(nx , ny))

        memory[i][j] = result+1
        return memory[i][j]

    ans = 0
    for x in range(n):
        for y in range(m):
            ans = max(ans , dfs(x , y))

    return ans

def main():

    test = int(input())

    for case in range(test):

        name , n , m = input().split()
        n , m = int(n) , int(m)
        arr = []

        for i in range(n):
            arr.append(list(map(int , input().split())))
        
        ans = solve(n , m , arr)
        print(f"{name}: {ans}")

if __name__ == "__main__":
    main()

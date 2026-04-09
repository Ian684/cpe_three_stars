from heapq import *
arr = []
n , m = None , None
ans = None

def dijkstra():
    global n , m , arr , ans
    q = [[arr[0][0] , 0 , 0]]
    heapify(q)
    directions = ((0,-1),(0,1),(1,0),(-1,0))
    check = [[False]*m for _ in range(n)]
    check[0][0] = True
    if n-1 == 0 and m-1 == 0:
        ans = arr[0][0]
        return
    while True:
        count , x , y = heappop(q)
        check[x][y] = True
        if x == n-1 and y == m-1:
            ans = count + arr[x][y]
            return
        for dx , dy in directions:
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
            if check[nx][ny]:continue
            heappush(q , [count + arr[nx][ny] , nx , ny])
    return 
def main():
    global n , m , arr , ans
    c = int(input())
    for i in range(c):
        n = int(input())
        m = int(input())
        arr = []
        for j in range(n):
            arr.append(list(map(int , input().split())))
        dijkstra()
        print(ans)
if __name__ == "__main__":
    main()

from heapq import *
from math import *

def time(h1 , h2 , a , b , b1 , b2):
    if h1 == h2:return b
    if h1 > h2:return ceil(b1*(h1-h2)) + b
    else:return ceil(b2*(h2-h1)) + b

def ener(h1 , h2 , a , b , a1 , a2):
    if h1 == h2:return a
    if h1 > h2:return ceil(a1*(h1-h2)) + a
    else:return ceil(a2*(h2-h1)) + a

def dijkstra(n , m , a1 , a2 , a , b1 , b2 , b , arr , startx , starty , endx , endy , energy):
    
    ans = 1 << 60
    q = []
    heapify(q)
    heappush(q , [0 , 0 , startx-1 , starty-1])

    dist = [[[1 << 60]*(energy+1) for i in range(m)] for _ in range(n)]
    dist[startx-1][starty-1][0] = 0
    while q:
        t , e , x , y = heappop(q)
        if x == endx-1 and y == endy-1:
            ans = t
            break
        if t > dist[x][y][e]:continue
        
        for dx , dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
            nt , ne = t+time(arr[x][y] , arr[nx][ny] , a , b , b1 , b2) , e+ener(arr[x][y] , arr[nx][ny] , a , b , a1 , a2)
            if ne > energy:continue
            if nt < dist[nx][ny][ne]:
                dist[nx][ny][ne] = nt
                heappush(q , [nt , ne , nx , ny])

    if ans == 1 << 60:return "failed"
    return ans

def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        a1 , a2 , a = input().split()
        a1 , a2 , a = float(a1) , float(a2) , int(a)
        b1 , b2 , b = input().split()
        b1 , b2 , b = float(b1) , float(b2) , int(b)
        arr = [list(map(int , input().split())) for _ in range(n)]
        startx , starty , endx , endy , energy = map(int , input().split())
        print(dijkstra(n , m , a1 , a2 , a , b1 , b2 , b , arr , startx , starty , endx , endy , energy))
if __name__ == "__main__":
    main()

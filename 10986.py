from heapq import *

def dijkstra(n , start , end , lines):

    q = []
    heappush(q , [0 , start])
    dis = [float('inf')]*n
    dis[start] = 0

    while q:
        lan , now = heappop(q)

        if lan != dis[now]:continue
        if now == end:return dis[end]

        if now not in lines:continue
        for _next , dlan in lines[now]:
            nlan = lan + dlan
            if nlan < dis[_next]:
                dis[_next] = nlan
                heappush(q , [nlan , _next])

    return "unreachable"
    

def main():
    test = int(input())
    for c in range(test):
        n , m , start , end = map(int , input().split())
        lines = {}
        for i in range(m):
            a , b , d = map(int , input().split())
            if a not in lines:
                lines[a] = []
            if b not in lines:
                lines[b] = []
            lines[a].append([b , d])
            lines[b].append([a , d])
        ans = dijkstra(n , start , end , lines)
        print(f"Case #{c+1}: {ans}")

if __name__ == "__main__":
    main()

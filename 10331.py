from heapq import *

def dijkstra(start , n , lines):

    hq = []
    heappush(hq , [0 , start])
    dis = [1 << 32]*n
    dis[start] = 0

    while hq:
        count , now = heappop(hq)

        if count != dis[now]:continue
        for _next , d in lines[now]:
            if count + d < dis[_next]:
                heappush(hq , [count + d , _next])
                dis[_next] = count + d

    return dis

def solve(n , l , lines , result):

    dis = []
    ans = [0]*l
    for start in range(n):
        dis.append(dijkstra(start , n , lines))

    for s in range(n):
        for t in range(s+1 , n):
            if dis[s][t] == 1 << 32:
                continue
            for i , (a , b , d) in enumerate(result):
                if (dis[s][a] + d + dis[b][t] == dis[s][t]) or (dis[s][b] + d + dis[a][t] == dis[s][t]):
                    ans[i] += 1

    return ans


def main():
    while True:
        try:
            n , l = map(int , input().split())
            result = []
            lines = {}
            for i in range(l):
                a , b , d = map(int , input().split())
                a -= 1
                b -= 1
                result.append([a , b , d])
                if a not in lines:
                    lines[a] = []
                if b not in lines:
                    lines[b] = []
                lines[a].append([b , d])
                lines[b].append([a , d])
        except EOFError:break

        ans = solve(n , l , lines , result)
        arr = []
        m = -1
        for i in range(l):
            if ans[i] > m:
                arr = [str(i+1)]
                m = ans[i]
            elif ans[i] == m:
                arr.append(str(i+1))
        print(' '.join(arr))

if __name__ == "__main__":
    main()

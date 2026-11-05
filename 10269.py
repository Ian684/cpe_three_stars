from heapq import *

def dijkstra(village , castle , l , k , lines):

    hq = []
    heappush(hq , [0 , village + castle - 1 , k , 0])

    dis = {}
    for i in range(village + castle):
        for j in range(k+1):
            for o in range(l+1):
                dis[(i , j , o)] = 1 << 32
    dis[(village + castle - 1 , k , 0)] = 0
    
    while hq:
        time , now , jump , remain = heappop(hq)

        if time != dis[(now , jump , remain)]:continue
        if now == 0:return time

        for _next , d in lines[now]:

            ntime = time + d
            if ntime < dis[(_next , jump , 0)]:
                heappush(hq , [ntime , _next , jump , 0])
                dis[(_next , jump , 0)] = ntime

            if l >= d and jump > 0:
                if _next >= village and time < dis[(_next , jump - 1 , 0)]: 
                    heappush(hq , [time , _next , jump - 1 , 0])
                    dis[(_next , jump - 1 , 0)] = time
                elif _next < village and time < dis[(_next , jump - 1 , l - d)]:
                    heappush(hq , [time , _next , jump - 1 , l - d])
                    dis[(_next , jump - 1 , l - d)] = time

            if remain >= d:
                if _next >= village and time < dis[(_next , jump , 0)]:
                    heappush(hq , [time , _next , jump , 0]) 
                    dis[(_next , jump , 0)] = time
                elif _next < village and time < dis[(_next , jump , remain - d)]:
                    heappush(hq , [time , _next , jump , remain - d]) 
                    dis[(_next , jump , remain - d)] = time

    return None

def main():
    test = int(input())
    for _ in range(test):
        village , castle , road , l , k = map(int , input().split())
        lines = [[] for i in range(village + castle)]
        for i in range(road):
            a , b , d = map(int , input().split())
            a -= 1
            b -= 1
            lines[a].append([b , d])
            lines[b].append([a , d])
        ans = dijkstra(village , castle , l , k , lines)
        print(ans)

if __name__ == "__main__":
    main()

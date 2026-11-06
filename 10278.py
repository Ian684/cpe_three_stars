from heapq import *

def dijkstra(fire , n , stations , lines):

    
    while hq:
        count , now = heappop(hq)
        if count != dis[now]:continue

        for _next , d in lines[now]:

            nd = count + d
            if nd < dis[_next]:
                dis[_next] = nd
                heappush(hq , [nd , _next])

    return dis
    
def main():
    test = int(input())
    line = input()
    for case in range(test):
        fire , n = map(int , input().split())
        stations = []
        for i in range(fire):
            stations.append(int(input())-1)
        lines = [[] for _ in range(n)]
        while True:
            try:
                line = input()
                if line == '':break
                a , b , d = map(int , line.split())
                a -= 1
                b -= 1
                lines[a].append([b , d])  
                lines[b].append([a , d])  
            except EOFError:break

        hq = []
        dis = [1 << 32]*n
        for i in range(fire):
            heappush(hq , [0 , stations[i]])
            dis[stations[i]] = 0
        d = dijkstra(fire , n , stations , lines , hq , dis)
        print(ans)
        if case != test - 1:print()

if __name__ == "__main__":
    main()

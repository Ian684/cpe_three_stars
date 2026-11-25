from heapq import *

def solve(v , lines):

    dis = []
    def dijkstra(start , lines):

        hq = []
        heappush(hq , [0 , start])
        d1 = [1 << 32]*v
        d1[start] = 0
        d2 = [1 << 32]*v

        while hq:
            count , n = heappop(hq)

            if count > d2[n]:continue
            for _next , d in lines[n]:

                dc = d + count
                if dc < d1[_next]:
                    heappush(hq , [dc , _next])
                    dc , d1[_next] = d1[_next] , dc
                if d1[_next] < dc < d2[_next]:
                    heappush(hq , [dc , _next])
                    d2[_next] = dc

        return d2

    for start in range(v):
        dis.append(dijkstra(start , lines))
    return dis

def main():
    now = 1
    while True:
        try:
            v , e  = map(int , input().split())
            lines = [[] for _ in range(v)]
            for i in range(e):
                a , b , d = map(int , input().split())
                lines[a].append([b , d])
                lines[b].append([a , d])
            dis = solve(v , lines)
            print(f"Set #{now}")
            now += 1
            q = int(input())
            for i in range(q):
                a , b = map(int , input().split())
                if dis[a][b] == 1 << 32:
                    print('?')
                else:
                    print(dis[a][b])
            line = input()
        except EOFError:break

if __name__ == "__main__":
    main()

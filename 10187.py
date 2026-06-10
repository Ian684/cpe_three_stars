from heapq import *

def dijkstra(lines , dis , start):
    q = []
    heapify(q)
    dis[start] = (0 , 18)
    heappush(q , [0 , 18 , start])
    while q:
        count , time , now = heappop(q)
        if (count , time) != dis[now]:
            continue
        
        if now not in lines:continue
        for _next , time1 , time2 in lines[now]:
            if time <= time1:
                cost = 0
            else:
                cost = 1
            if count + cost < dis[_next][0]:
                dis[_next] = (count + cost , time2)
                heappush(q , [count+cost , time2 , _next])
            elif count + cost == dis[_next][0] and time2 < dis[_next][1]:
                dis[_next] = (count + cost , time2)
                heappush(q , [count+cost , time2 , _next])
    return dis


def main():
    test = int(input())
    for t in range(test):
        n = int(input())
        lines = {}
        dis = {}
        for i in range(n):
            a , b , start , time = input().split()
            start , end = int(start) , int(start)+int(time)
            if int(time) <= 12:
                end %= 24
                if (start >= 18 or start <= 6) and (end >= 18 or end <= 6):
                    if a not in lines:
                        lines[a] = []
                    if start <= 6:
                        start += 24
                    if end <= 6:
                        end += 24
                    lines[a].append([b , start , end])
            if a not in dis:
                dis[a] = (1 << 60 , 1 << 60)
            if b not in dis:
                dis[b] = (1 << 60 , 1 << 60)
        start , end = input().split()
        if start not in dis:
            dis[start] = (1 << 60 , 1 << 60)
        if end not in dis:
            dis[end] = (1 << 60 , 1 << 60)
        dis = dijkstra(lines , dis , start)
        ans = dis[end][0]
        print(f"Test Case {t+1}.")
        if ans == 1 << 60:
            print("There is no route Vladimir can take.")
        else:
            print(f"Vladimir needs {ans} litre(s) of blood.")

if __name__ == "__main__":
    main()

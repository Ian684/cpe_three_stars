from collections import deque
lines = {}
n , start = None , None
count , final = None , None

def bfs():
    global lines , final , count , n , start
    q = deque([start])
    dist = [-1]*(n+1)
    dist[start] = 0
    while q:
        now = q.popleft()
        for _next in lines[now]:
            if dist[_next] < dist[now] + 1:
                dist[_next] = dist[now] + 1
                q.append(_next)
    count = max(dist)
    for i in range(1 , n+1):
        if dist[i] == count:
            final = min(final , i)
    return
def main():
    global lines , final , count , start , n
    c = 1
    while True:
        n = int(input())
        if n == 0:break
        start = int(input())
        lines = {}
        for i in range(1 , n+1):
            lines[i] = []
        while True:
            a , b = map(int , input().split())
            if a == 0 and b == 0:break
            lines[a].append(b)
        count = 0
        final = 1 << 60
        bfs()
        print(f"Case {c}: The longest path from {start} has length {count}, finishing at {final}.")
        print()
        c += 1

if __name__ == "__main__":
    main()

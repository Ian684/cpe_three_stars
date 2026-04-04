from collections import deque
n , r = None , None
lines = {}
start , end = None , None
check = set()
def bfs():
    global n , r , lines , start , end , check
    q = deque([[start , 1 << 60]])
    check.add(start)
    result = -1
    while q:
        city , point = q.popleft()
        if city not in lines:
            continue
        for l , npoint in lines[city]:
            if l in check:continue
            if end == l:
                result = max(result , min(point , npoint))
                continue
            check.add(l)
            q.append([l , min(point , npoint)])
    return result
def main():
    global n , r , lines , start , end , check
    now = 1
    while True:
        n , r = map(int , input().split())
        if n == 0 and r == 0:break
        lines = {}
        check = set()
        for i in range(r):
            a , b , point = input().split()
            point = int(point)
            if a not in lines:
                lines[a] = []
            if b not in lines:
                lines[b] = []
            lines[a].append([b , point])
            lines[b].append([a , point])
        start , end = input().split()
        result = bfs()
        print(f"Scenario #{now}")
        print(f"{result} tons")
        print()
        now += 1
if __name__ == "__main__":
    main()

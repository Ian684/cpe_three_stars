from math import *
from collections import deque

def bfs(lines , start , end):
    q = deque([])
    q.append([start , 1 , 1])
    visited = set()
    visited.add(start)

    while q:
        now , _n , _m = q.popleft()

        for n , m , _next in lines[now]:
            if _next in visited:continue
            if _next == end:return [_n*n , _m*m]
            visited.add(_next)
            q.append([_next , _n*n , _m*m])

    return None

def main():

    lines = {}
    while True:
        try:
            line = input()
            if line == '.':break
            line = line.split()
            command = line[0]
            if command == "!":
                n , a , trash , m , b = line[1:]
                n , m = int(n) , int(m)
                if a not in lines:
                    lines[a] = []
                if b not in lines:
                    lines[b] = []
                lines[a].append([n , m , b])
                lines[b].append([m , n , a])
            else:
                a , trash , b = line[1:]
                ans = bfs(lines , a , b)
                if ans is None:
                    print(f"? {a} = ? {b}")
                    continue
                g = gcd(ans[0] , ans[1])
                print(f"{ans[0]//g} {a} = {ans[1]//g} {b}")

        except EOFError:break

if __name__ == "__main__":
    main()

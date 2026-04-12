from copy import *
from collections import deque
alph = {}

def bfs(start , end):
    global alph
    q = deque([start])
    check = set()
    check.add(start)
    while q:
        now = q.popleft()
        for _next in alph[now]:
            if _next in check:continue
            if _next == end:
                return True
            check.add(_next)
            q.append(_next)
    return False

def generate():
    origin = {}
    for i in range(97 , 123):
        origin[chr(i)] = set()
    return origin

def main():
    global alph
    origin = generate()
    while True:
        try:
            n , m = map(int , input().split())
        except EOFError:break
        alph = deepcopy(origin)
        for i in range(n):
            a , b = input().split()
            alph[a].add(b)
        for i in range(m):
            a , b = input().split()
            if len(a) != len(b):
                print("no")
                continue
            flag = True
            for l in range(len(a)):
                if a[l] == b[l]:
                    continue
                if bfs(a[l] , b[l]):
                    continue
                else:
                    flag = False
                    break
            if flag:
                print("yes")
            else:
                print("no")
if __name__ == "__main__":
    main()

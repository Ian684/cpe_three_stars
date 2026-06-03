from heapq import *

def dijkstra(lines , start , check):

    hq = []
    heapify(hq)
    heappush(hq , [0 , start])
    check[start] = 0

    while hq:
        w , now = heappop(hq)
        if check[now] != w:continue

        if now not in lines:continue
        for _next , dw in lines[now]:
            nw = w + dw
            if nw < check[_next]:
                check[_next] = nw
                heappush(hq , [nw , _next])
    
    return check

def solve(lines1 , lines2 , start , end , check1 , check2):

    check1 = dijkstra(lines1 , start , check1)
    check2 = dijkstra(lines2 , end , check2)

    ans = [1 << 60]
    for k , v in check1.items():
        if k not in check2:continue
        nans = v + check2[k]
        if nans < ans[0]:
            ans = [nans , k]
        elif nans == ans[0]:
            ans.append(k)
    if ans[0] == 1 << 60:
        return None
    return ans

def main():
    while True:
        n = int(input())
        if n == 0:break
        lines1 = {}
        lines2 = {}
        check1 = {}
        check2 = {}
        for i in range(n):
            c1 , c2 , a , b , w = input().split()
            w = int(w)
            if c1 == 'Y':
                if a not in check1:
                    check1[a] = 1 << 60
                if b not in check1:
                    check1[b] = 1 << 60
                if c2 == 'U':
                    if a not in lines1:
                        lines1[a] = []
                    lines1[a].append([b , w])
                else:
                    if a not in lines1:
                        lines1[a] = []
                    if b not in lines1:
                        lines1[b] = []
                    lines1[a].append([b , w])
                    lines1[b].append([a , w])
            else:
                if a not in check2:
                    check2[a] = 1 << 60
                if b not in check2:
                    check2[b] = 1 << 60
                if c2 == 'U':
                    if a not in lines2:
                        lines2[a] = []
                    lines2[a].append([b , w])
                else:
                    if a not in lines2:
                        lines2[a] = []
                    if b not in lines2:
                        lines2[b] = []
                    lines2[a].append([b , w])
                    lines2[b].append([a , w])
        start , end = input().split()
        ans = solve(lines1 , lines2 , start , end , check1 , check2)
        if ans is None:
            print("You will never meet.")
        else:
            print(' '.join(map(str , ans)))

if __name__ == "__main__":
    main()

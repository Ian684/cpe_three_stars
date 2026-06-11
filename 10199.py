import sys
sys.setrecursionlimit(2000)

timer = 0
dfn = {}
low = {}
lines = {}
is_cut = {}
names = []

def tarjan(now , parent):
    global timer , dfn , low , lines , is_cut , names
    dfn[now] = timer
    low[now] = timer
    children = 0
    timer += 1
    if now in lines:
        for _next in lines[now]: 
            if dfn[_next] == -1:
                children += 1
                tarjan(_next , now)
                low[now] = min(low[_next] , low[now])
                if parent != -1 and low[_next] >= dfn[now]:
                    is_cut[now] = True

            elif dfn[_next] != -1 and parent != _next:
                low[now] = min(dfn[_next] , low[now])
        if parent == -1 and children > 1:
            is_cut[now] = True

def main():
    global timer , dfn , low , lines , is_cut , names
    now = 1
    first = True
    while True:
        n = int(input())
        if n == 0:break
        names = []
        for i in range(n):
            temp = input()
            names.append(temp)
            dfn[temp] = -1
            low[temp] = -1
            is_cut[temp] = False
        route = int(input())
        lines = {}
        for i in range(route):
            a , b = input().split()
            if a not in lines:
                lines[a] = []
            if b not in lines:
                lines[b] = []
            lines[a].append(b)
            lines[b].append(a)
        timer = 0
        for name in names:
            if dfn[name] != -1:continue
            tarjan(name , -1)
        ans = []
        for name in names:
            if is_cut[name]:
                ans.append(name)
        if first:first = False
        else:print()
        print(f"City map #{now}: {len(ans)} camera(s) found")
        now += 1
        ans = sorted(ans)
        for a in ans:
            print(a)

if __name__ == "__main__":
    main()

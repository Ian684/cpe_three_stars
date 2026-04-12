from collections import deque
lines = {}
_in = {}
n , start = None , None
count , final = None , None

def topo():
    global lines , _in , final , count , n , start
    q = deque([])
    for i in range(1 , n+1):
        if _in[i] == 0:
            q.append(i)
    ans = []
    while q:
        now = q.popleft()
        ans.append(now)
        for _next in lines[now]:
            _in[_next] -= 1
            if _in[_next] == 0:
                q.append(_next)
    dp = [-1]*(n+1)
    dp[start] = 0
    for u in ans:
        if dp[u] == -1:continue
        for v in lines[u]:
            dp[v] = max(dp[v] , dp[u]+1)
    best_len = 0
    best_node = start
    
    for i in range(1 , n+1):
        if dp[i] > best_len:
            best_len = dp[i]
            best_node = i
        elif dp[i] == best_len and i < best_node:
            best_node = i

    final = best_node
    count = best_len
    return
def main():
    global lines , _in , final , count , start , n
    c = 1
    while True:
        n = int(input())
        if n == 0:break
        start = int(input())
        lines = {}
        _in = {}
        for i in range(1 , n+1):
            lines[i] = []
            _in[i] = 0
        while True:
            a , b = map(int , input().split())
            if a == 0 and b == 0:break
            lines[a].append(b)
            _in[b] += 1
        final = -1
        count = 0
        topo()
        print(f"Case {c}: The longest path from {start} has length {count}, finishing at {final}.")
        print()
        c += 1

if __name__ == "__main__":
    main()

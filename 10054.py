import sys
sys.setrecursionlimit(2000)
def solve(n , lines , a , check):
    ans = []

    def dfs(now):
        nonlocal ans
        for _next in lines[now]:
            if check[(now , _next)] == 0:continue
            check[(now , _next)] -= 1
            check[(_next , now)] -= 1
            dfs(_next)
            ans.append([now , _next])
        
    dfs(a)
    return ans

def main():
    c = int(input())
    for i in range(c):
        n = int(input())
        lines = {}
        check = {}
        degree = {}
        for j in range(n):
            a , b = map(int , input().split())
            if a not in lines:
                lines[a] = []
            if b not in lines:
                lines[b] = []
            lines[a].append(b)
            lines[b].append(a)
            if (a , b) not in check:
                check[(a , b)] = 0
            if (b , a) not in check:
                check[(b , a)] = 0
            check[(a , b)] += 1
            check[(b , a)] += 1
            if a not in degree:
                degree[a] = 0
            if b not in degree:
                degree[b] = 0
            degree[a] += 1
            degree[b] += 1
        flag = True
        for k , v in degree.items():
            if v & 1:
                flag = False
                break
        print(f"Case #{i+1}")
        if not flag:
            print("some beads may be lost")
        else:
            ans = solve(n , lines , a , check)
            if len(ans) != n:
                print("some beads may be lost")
            else:
                for a , b in ans:
                    print(a , b)
        if i != c - 1:print()
if __name__ == "__main__":
    main()

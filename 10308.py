def solve(lines):

    ans = 0

    def dfs(now , parent):
        nonlocal ans

        top1 = 0
        top2 = 0
        for _next , d in lines[now]:
            if _next == parent:continue

            l = dfs(_next , now) + d

            if l > top1:
                top1 , top2 = l , top1
            elif l > top2:
                top2 = l

        ans = max(ans , top1 + top2)
        return top1

    dfs(1 , -1)
    return ans


def main():
    while True:
        
        lines = {}
        count = 0
        while True:
            try:
                line = input()
                if line == '':break
                a , b , d = map(int , line.split())
                count += 1
                if a not in lines:
                    lines[a] = []
                if b not in lines:
                    lines[b] = []
                lines[a].append([b , d])
                lines[b].append([a , d])
            except EOFError:break
        if count == 0:break
        
        ans = solve(lines)
        print(ans)

if __name__ == "__main__":
    main()

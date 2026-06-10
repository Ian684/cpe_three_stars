def solve(n , names , lines , ans):

    def dfs1(aim , now):
        if now >= len(lines):
            rank = 1
            value = names[aim][0]
            for k , v in names.items():
                if v[0] > value:
                    rank += 1
            ans[aim][0] = min(ans[aim][0] , rank)
            return 
        a , b = lines[now]
        if a == aim:
            names[a][0] += 3
            dfs1(aim , now+1)
            names[a][0] -= 3
        elif b == aim:
            names[b][0] += 3
            dfs1(aim , now+1)
            names[b][0] -= 3
        else:
            names[a][0] += 1
            names[b][0] += 1
            dfs1(aim , now+1)
            names[a][0] -= 1
            names[b][0] -= 1
            names[a][0] += 3
            dfs1(aim , now+1)
            names[a][0] -= 3
            names[b][0] += 3
            dfs1(aim , now+1)
            names[b][0] -= 3
    def dfs2(aim , now):
        if now >= len(lines):
            rank = 0
            value = names[aim][0]
            for k , v in names.items():
                if v[0] >= value:
                    rank += 1
            ans[aim][1] = max(ans[aim][1] , rank)
            return 
        a , b = lines[now]
        if a == aim:
            names[b][0] += 3
            dfs2(aim , now+1)
            names[b][0] -= 3
        elif b == aim:
            names[a][0] += 3
            dfs2(aim , now+1)
            names[a][0] -= 3
        else:
            names[a][0] += 1
            names[b][0] += 1
            dfs2(aim , now+1)
            names[a][0] -= 1
            names[b][0] -= 1
            names[a][0] += 3
            dfs2(aim , now+1)
            names[a][0] -= 3
            names[b][0] += 3
            dfs2(aim , now+1)
            names[b][0] -= 3


    for k , v in ans.items():
        dfs1(k , 0)
        dfs2(k , 0)
    return ans

def main():
    now = 1
    while True:
        n = int(input())
        if n == 0:break
        names = {}
        _names = []
        ans = {}
        for i in range(n):
            temp = input()
            names[temp] = [0 , 0 , 0]
            ans[temp] = [1 << 60 , -1]
            # points , goals get , goals lose
            _names.append(temp)
        pk = set()
        for i in range(n):
            for j in range(i+1,n):
                pk.add((_names[i] , _names[j] , 1))
                pk.add((_names[i] , _names[j] , 2))
        q = int(input())
        for i in range(q):
            a , b , ap , bp = input().split()
            if (a , b , 1) not in pk and (b , a , 1) not in pk:
                if (a , b , 2) in pk:
                    pk.remove((a , b , 2))
                else:
                    pk.remove((b , a , 2))
            else:
                if (a , b , 1) in pk:
                    pk.remove((a , b , 1))
                else:
                    pk.remove((b , a , 1))
            ap , bp = int(ap) , int(bp)
            if ap > bp:
                names[a][0] += 3
            elif ap < bp:
                names[b][0] += 3
            else:
                names[a][0] += 1
                names[b][0] += 1
            names[a][1] += ap
            names[a][2] += bp
            names[b][1] += bp
            names[b][2] += ap
        lines = []
        for a , b , d in pk:
            lines.append([a , b])
        ans = solve(n , names , lines , ans)
        print(f"Group #{now}")
        now += 1
        for k , v in ans.items():
            print(f"{k} {v[0]}-{v[1]}")
        print()

if __name__ == "__main__":
    main()

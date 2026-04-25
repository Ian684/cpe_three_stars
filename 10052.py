import sys
sys.setrecursionlimit(2000)

def solve(memo , names , man , conflict  , n , m):
    ans = [[],[],[],[]]
    now = 0
    def dfs(now):
        if now >= len(names):
            return True
        if len(memo[names[now]]) == 0:return False
        for col in list(memo[names[now]]):
            temp = set()
            man[names[now]] = col
            flag = True
            for con in conflict[names[now]]:
                if col not in memo[con]:continue
                memo[con].remove(col)
                temp.add((con , col))
                if len(memo[con]) == 0:
                    flag = False
                    break
            if flag:
                if dfs(now+1):
                    ans[col].append(names[now])
                    return True
            for a , b in temp:
                memo[a].add(b)
        return False
    dfs(now)
    return ans
def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    t = int(next(tokens))
    for i in range(t):
        n , m = int(next(tokens)) , int(next(tokens))
        man = {}
        names = []
        conflict = {}
        memo = {}
        for j in range(n):
            temp = next(tokens)
            names.append(temp)
            man[temp] = -1
            conflict[temp] = set()
            memo[temp] = set([0 , 1 , 2 , 3])
        for j in range(m):
            a , b = next(tokens) , next(tokens)
            conflict[a].add(b)
            conflict[b].add(a)
        ans = solve(memo , names , man , conflict , n , m)
        print(f"Case #{i+1}")
        for a in ans:
            print(len(a))
            print(' '.join(a))
        if i != t-1:print()
if __name__ == "__main__":
    main()

def output(ans , u):
    print(f"max coverage = {' '*(3-len(str(u)))}{u} :" , end="")
    for a in ans:
        print(f"{' '*(3-len(str(a)))}{a}" , end="")
    print()
def solve(stamps , s):
    result = []
    b = 1001
    for st in stamps:
        dp = [1 << 60]*(b+1)
        dp[0] = 0
        for w in st:
            dp[w] = 1
        for w in st:
            for i in range(w , b+1):
                dp[i] = min(dp[i] , dp[i-w]+1)
        for i in range(1 , b+1):
            if dp[i] > s:
                result.append(i-1)
                break
    return result
def main():
    while True:
        s = int(input())
        if s == 0:break
        q = int(input())
        stamps = []
        for i in range(q):
            stamps.append(list(map(int , input().split()[1:])))
        result = solve(stamps , s)
        ans = []
        u = -1
        for i in range(q):
            if result[i] > u:
                ans = [stamps[i]]
                u = result[i]
            elif result[i] == u:
                ans.append(stamps[i])
        if len(ans) == 1:
            output(ans[0] , u)
        else:
            ul = None
            l = 1 << 60
            for i in ans:
                if len(i) < l:
                    ul = i[::]
                    l = len(i)
                elif len(i) == l:
                    ul = sorted([ul[::-1] , i[::-1]])[0][::-1]
            output(ul , u)
if __name__ == "__main__":
    main()

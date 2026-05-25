def main():
    elephants = []
    i = 1
    while True:
        try:
            elephants.append(list(map(int , input().split()))+[i])
            i += 1
        except EOFError:break
    elephants = sorted(elephants , key = lambda x : (x[0] , -x[1]))
    n = len(elephants)
    dp = [1]*n
    parent = [-1]*n
    for i in range(n):
        for j in range(i):
            if elephants[j][1] > elephants[i][1] and elephants[j][0] < elephants[i][0]:
                if dp[j] + 1 > dp[i]:
                    parent[i] = j
                    dp[i] = dp[j]+1
    ml = max(dp)
    print(ml)
    ans = []
    cur = dp.index(ml)
    while cur != -1:
        ans.append(elephants[cur][2])
        cur = parent[cur]

    for a in ans[::-1]:
        print(a)
    
if __name__ == "__main__":
    main()

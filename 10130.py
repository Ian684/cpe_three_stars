def solve(mw , goods , value , weight):
    dp = [0]*(mw+1)
    for i in range(goods):
        v = value[i]
        w = weight[i]
        for j in range(mw , w-1 , -1):
            dp[j] = max(dp[j] , dp[j-w]+v)
    return dp[mw]

def main():
    t = int(input())
    for _ in range(t):
        goods = int(input())
        value = []
        weight = []
        for i in range(goods):
            v , w = map(int , input().split())
            value.append(v)
            weight.append(w)
        people = int(input())
        ans = 0
        for i in range(people):
            mw = int(input())
            ans += solve(mw , goods , value , weight)
        print(ans)

if __name__ == "__main__":
    main()

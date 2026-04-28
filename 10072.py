def solve(players , bt , bl , ar):
    dp = [[[[-1]*(ar+1) for b in range(bl+1)] for a in range(bt+1)] for i in range(len(players)+1)]
    dp[0][0][0][0] = 0
    choice = [[[[-1]*(ar+1) for b in range(bl+1)] for a in range(bt+1)] for i in range(len(players)+1)]
    result1 , result2 , result3 = [] , [] , []
    for i in range(1 , len(players)+1):
        for a in range(bt+1):
            for b in range(bl+1):
                for c in range(ar+1):
                    if i > 0 and dp[i-1][a][b][c] != -1:
                        be_none = dp[i-1][a][b][c]
                        if be_none > dp[i][a][b][c]:
                            dp[i][a][b][c] = be_none
                            choice[i][a][b][c] = 0
                    if a > 0 and dp[i-1][a-1][b][c] != -1:
                        be_bt = dp[i-1][a-1][b][c]+players[i-1][0]
                        if be_bt > dp[i][a][b][c]:
                            dp[i][a][b][c] = be_bt
                            choice[i][a][b][c] = 1
                    if b > 0 and dp[i-1][a][b-1][c] != -1:
                        be_bl = dp[i-1][a][b-1][c]+players[i-1][1]
                        if be_bl > dp[i][a][b][c]:
                            dp[i][a][b][c] = be_bl
                            choice[i][a][b][c] = 2
                    if c > 0 and dp[i-1][a][b][c-1] != -1:
                        be_ar = dp[i-1][a][b][c-1]+players[i-1][2]
                        if be_ar > dp[i][a][b][c]:
                            dp[i][a][b][c] = be_ar
                            choice[i][a][b][c] = 3

    a , b , c = bt , bl , ar
    # 為什麼可以這樣回溯
    for i in range(len(players) , 0 , -1):
        ch = choice[i][a][b][c]

        if ch == 1:
            result1.append(i)
            a -= 1
        if ch == 2:
            result2.append(i)
            b -= 1
        if ch == 3:
            result3.append(i)
            c -= 1
    return dp[-1][-1][-1][-1] , result1[::-1] , result2[::-1] , result3[::-1]


def main():
    now = 0
    first = True
    while True:
        c = int(input())
        if c == 0:break
        players = []
        for i in range(c):
            bt , bl , fl = map(int , input().split())
            players.append([int(0.8*bt+0.2*fl + 0.5) , int(0.7*bl+0.1*bt+0.2*fl + 0.5) , int(0.4*bt+0.4*bl+0.2*fl + 0.5)])
        bt , bl , ar = map(int , input().split())
        ans , result1 , result2 , result3 = solve(players , bt , bl , ar)
        if first:first = False
        else:print()
        print(f"Team #{now+1}")
        now += 1
        print(f"Maximum Effective Score = {ans}")
        print(f"Batsmen : {' '.join(map(str , result1))}")
        print(f"Bowlers : {' '.join(map(str , result2))}")
        print(f"All-rounders : {' '.join(map(str , result3))}")
if __name__ == "__main__":
    main()

def solve(players , bt , bl , ar):
    ans = -1
    result = ()
    def third_br(count3 , buf , check , total):
        nonlocal result , ans
        if count3 <= 0:
            if ans < total:
                ans = total
                result = buf
            return
        for i in range(len(players)):
            if check[i]:continue
            check[i] = True
            third_br(count3 - 1 , buf+(i+1 , ) , check , total+players[i][2])
            check[i] = False
        return

    def second_bl(count2 , buf , check , total):
        if count2 <= 0:
            third_br(ar , buf , check , total)
            return
        for i in range(len(players)):
            if check[i]:continue
            check[i] = True
            second_bl(count2 - 1 , buf+(i+1 , ) , check , total+players[i][1])
            check[i] = False
        return

    def first_bt(count1 , buf , check , total):
        if count1 <= 0:
            second_bl(bl , buf , check , total)
            return
        for i in range(len(players)):
            if check[i]:continue
            check[i] = True
            first_bt(count1 - 1 , buf+(i+1 , ) , check , total+players[i][0])
            check[i] = False
        return
    check = [False]*len(players)
    first_bt(bt , () , check , 0)

    return ans , result

def main():
    now = 0
    first = True
    while True:
        c = int(input())
        if c == 0:break
        players = []
        for i in range(c):
            bt , bl , fl = map(int , input().split())
            players.append([round(0.8*bt+0.2*fl) , round(0.7*bl+0.1*bt+0.2*fl) , round(0.4*bt+0.4*bl+0.2*fl)])
        bt , bl , ar = map(int , input().split())
        ans , result = solve(players , bt , bl , ar)
        if first:first = False
        else:print()
        print(f"Team #{now+1}")
        now += 1
        print(f"Maximum Effective Score = {ans}")
        print(f"Batsmen : {' '.join(map(str , result[:bt]))}")
        print(f"Bowlers : {' '.join(map(str , result[bt:bt+bl]))}")
        print(f"All-rounders : {' '.join(map(str , result[bt+bl:]))}")
if __name__ == "__main__":
    main()

from collections import deque
import sys
sys.setrecursionlimit(2000)
memo = {}
# memorize it all status

def dfs(aim , now , a , b , acum):
    global memo

    if now >= len(aim):
        if a == b:
            return 1
        else:
            return 2

    t = aim[now]
    if (now , acum) in memo:
        return memo[(now , acum)]

    best = 3
    if len(acum) < 10:
        best = min(best , dfs(aim , now+1 , a+1 , b , acum+(t,)))

    if best != 1 and acum and acum[0] == t:
        best = min(best , dfs(aim , now+1 , a , b+1 , acum[1:]))

    memo[(now , acum)] = best
    return best

def main():
    global memo
    c = int(input())
    for _ in range(c):
        aim = input()
        memo = {}
        status = dfs(aim , 0 , 0 , 0 , ())
        if status == 1:
            print("An echo string with buffer size ten")
        elif status == 2:
            print("Not an echo string, but still consistent with the theory")
        elif status == 3:
            print("Not consistent with the theory")

if __name__ == "__main__":
    main()

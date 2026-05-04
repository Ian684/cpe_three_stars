from math import *
import sys

def solve(start , end , node , lines):
    dp = [[-1]*(node+1) for _ in range(node+1)]
    for i in range(1 , node+1):
        dp[i][i] = 0
    for k , v in lines.items():
        dp[k[0]][k[1]] = v
        dp[k[1]][k[0]] = v
    for k in range(1 , node+1):
        for i in range(1 , node+1):
            for j in range(1 , node+1):
                dp[i][j] = max(dp[i][j] , min(dp[i][k] , dp[k][j]))

    return dp[start][end]

def main():
    now = 0
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    while True:
        try:
            node , line = int(next(tokens)) , int(next(tokens))
            if node == 0 and line == 0:break
            lines = {}
            for l in range(line):
                a , b , p = int(next(tokens)) , int(next(tokens)) , int(next(tokens))
                lines[(a , b)] = p
                lines[(b , a)] = p
            start , end , people = int(next(tokens)) , int(next(tokens)) , int(next(tokens))
            ans = solve(start , end , node , lines)
            print(f"Scenario #{now+1}")
            now += 1
            if ans > 1:
                print(f"Minimum Number of Trips = {ceil(people/(ans-1))}")
            else:
                print(f"Minimum Number of Trips = {0}")
            print()
        except EOFError:break
if __name__ == "__main__":
    main()

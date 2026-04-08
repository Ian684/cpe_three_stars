def main():
    c = int(input())
    for i in range(c):
        n = int(input())
        start = list(map(int , input().split()))
        end = list(map(int , input().split()))
        start = [start[0]-1 , start[1]-1]
        end = [end[0]-1 , end[1]-1]
        m = int(input())
        sp = [[set() for a in range(n+1)] for b in range(n+1)]
        for j in range(m):
            x , y , d = input().split()
            y , x = int(y)-1 , int(x)-1
            if d == "S":
                sp[x][y].add("S")
            elif d == "N":
                sp[x][y+1].add("S")
            elif d == "W":
                sp[x][y].add("W")
            elif d == "E":
                sp[x+1][y].add("W")
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[start[0]][start[1]] = 1
        for x in range(start[0] , end[0]+1):
            for y in range(start[1] , end[1]+1):
                if "W" not in sp[x][y] and x-1 >= start[0]:
                    dp[x][y] += dp[x-1][y]
                if "S" not in sp[x][y] and y-1 >= start[1]:
                    dp[x][y] += dp[x][y-1]
        print(dp[end[0]][end[1]])
if __name__ == "__main__":
    main()

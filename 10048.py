def main():
    now = 0
    first = True
    while True:
        c , s , q = map(int , input().split())
        if c == 0 and s == 0 and q == 0:break
        dist = [[1 << 60]*(c+1) for _ in range(c+1)]
        for i in range(s):
            a , b , sound = map(int , input().split())
            dist[a][b] = min(dist[a][b] , sound)
            dist[b][a] = min(dist[a][b] , sound)
        for k in range(1 , c+1):
            for i in range(1 , c+1):
                for j in range(1 , c+1):
                    if i == j:dist[i][j] = 0
                    dist[i][j] = min(dist[i][j] , max(dist[i][k] , dist[k][j]))
        if first:first = False
        else:print()
        print(f"Case #{now+1}")
        now += 1
        for i in range(q):
            a , b = map(int , input().split())
            if dist[a][b] >= 1 << 60:
                print("no path")
                continue
            print(dist[a][b])
if __name__ == "__main__":
    main()

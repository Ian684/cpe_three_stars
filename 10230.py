arr = []

def check(x , y , ax , ay , bx , by):
    global arr
    used = set()
    for dx in range(ax , bx+1):
        for dy in range(ay , by+1):
            if dx == x and dy == y:
                continue
            for ddx , ddy in ((0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)):
                nx , ny = dx + ddx , dy + ddy
                if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):continue
                used.add(arr[nx][ny])
    for i in range(26):
        al = chr(i+97)
        if al not in used:
            for dx in range(ax , bx+1):
                for dy in range(ay , by+1):
                    if dx == x and dy == y:
                        continue
                    arr[dx][dy] = al
            return 

def solve(n , x , y , ax , ay , bx , by):
    global arr
    if n <= 1:
        check(x , y , ax , ay , bx , by)
        return
    midx , midy = (ax + bx)//2 , (ay + by)//2
    p = [
        [midx , midy],
        [midx , midy+1],
        [midx+1 , midy],
        [midx+1 , midy+1]
    ]
    if x <= midx and y <= midy:
        check(p[0][0] , p[0][1] , p[0][0] , p[0][1] , p[3][0] , p[3][1])
        p[0] = [x , y]
    elif x <= midx and y > midy:
        check(p[1][0] , p[1][1] , p[0][0] , p[0][1] , p[3][0] , p[3][1])
        p[1] = [x , y]
    elif x > midx and y <= midy:
        check(p[2][0] , p[2][1] , p[0][0] , p[0][1] , p[3][0] , p[3][1])
        p[2] = [x , y]
    else:
        check(p[3][0] , p[3][1] , p[0][0] , p[0][1] , p[3][0] , p[3][1])
        p[3] = [x , y]
    solve(n-1 , p[0][0] , p[0][1] , ax , ay , midx , midy)
    solve(n-1 , p[1][0] , p[1][1] , ax , midy+1 , midx , by)
    solve(n-1 , p[2][0] , p[2][1] , midx+1 , ay , bx , midy)
    solve(n-1 , p[3][0] , p[3][1] , midx+1 , midy+1 , bx , by)
    return 

def main():
    global arr
    while True:
        try:
            n , y , x = map(int , input().split())
        except EOFError:break
        y -= 1
        x -= 1
        arr = [['']*(2**n) for _ in range(2**n)]
        solve(n , x , y , 0 , 0 , 2**n-1 , 2**n-1)
        arr[x][y] = '*'
        for i in range(2**n):
            print(''.join(arr[i]))
        print()

if __name__ == "__main__":
    main()

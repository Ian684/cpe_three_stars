from collections import deque
arr = []
check = []
start = None
end = None
h , x , y = None , None , None
count = None
directions = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
def bfs():
    global arr , check , start , end , h , x , y , count , directions
    q = deque([start+[0]])
    check[start[0]][start[1]][start[2]] = True
    while q:
        a , b , c , step = q.popleft()
        for dh , dx , dy in directions:
            nh , nx , ny = a + dh , b + dx , c + dy
            if nh < 0 or nh >= h or nx < 0 or nx >= x or ny < 0 or ny >= y:continue
            if check[nh][nx][ny]:
                continue
            if [nh , nx , ny] == end:
                count = step + 1
                return True
            check[nh][nx][ny] = True
            q.append([nh , nx , ny , step+1])
    return False
def main():
    global arr , check , start , end , h , x , y , count
    while True:
        h , x , y = map(int , input().split())
        if h == 0 and x == 0 and y == 0:break
        start = None
        end = None
        arr = []
        count = 0
        check = [[[False]*y for i in range(x)] for j in range(h)]
        for i in range(h):
            arr.append([])
            for j in range(x):
                arr[i].append(input())
                for k in range(y):
                    if arr[i][j][k] == "S":
                        start = [i , j , k]
                    elif arr[i][j][k] == "E":
                        end = [i , j , k]
                    elif arr[i][j][k] == "#":
                        check[i][j][k] = True
            blank_line = input()
        if bfs():
            print(f"Escaped in {count} minute(s).")
        else:
            print("Trapped!")
if __name__ == "__main__":
    main()

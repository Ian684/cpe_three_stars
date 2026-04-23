from collections import deque

def bfs(color , arr , end , check , x , y , direction , count):
    check[(x , y)].add((color , direction))
    q = deque([])
    q.append([x , y , direction , count , color])
    while q:
        x , y , direction , count , color = q.popleft()
        left = (direction + 1)%4
        if (color , left) not in check[(x , y)]:
            q.append([x , y , left , count+1 , color])
            check[(x , y)].add((color , left))
        right = (direction + 3)%4
        if (color , right) not in check[(x , y)]:
            q.append([x , y , right , count+1 , color])
            check[(x , y)].add((color , right))
        if direction == 0:
            dx , dy = -1 , 0
        elif direction == 1:
            dx , dy = 0 , 1
        elif direction == 2:
            dx , dy = 1 , 0
        elif direction == 3:
            dx , dy = 0 , -1
        nx , ny = x + dx , y + dy
        next_color = (color + 1) % 5
        if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr[0]):continue
        if arr[nx][ny] == "#":continue
        if (next_color , direction) in check[(nx , ny)]:continue
        if (nx , ny) == end and next_color == 0:return count+1
        check[(nx , ny)].add((next_color , direction))
        q.append([nx , ny , direction , count+1 , next_color])
    return 

def main():
    now = 1
    first = True
    while True:
        try:
            n , m = map(int , input().split())
            if n == 0 and m == 0:break
            arr = []
            check = {}
            all_ = set()
            for i in range(n):
                t = input()
                arr.append(t)
                for j in range(m):
                    if t[j] == '#':
                        check[(i , j)] = None
                        continue
                    elif t[j] == 'S':
                        start = (i , j)
                    elif t[j] == 'T':
                        end = (i , j)
                    check[(i , j)] = set()
        except EOFError:break
        direction = 0
        # 0 1 2 3
        count = 0
        color = 0
        count = bfs(color , arr , end , check , start[0] , start[1] , direction , count)
        if first:first = False
        else:print()
        print(f"Case #{now}")
        now += 1
        if count is None:
            print("destination not reachable")
        else:
            print(f"minimum time = {count} sec")
if __name__ == "__main__":
    main()

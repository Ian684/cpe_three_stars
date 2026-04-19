from collections import deque

def bfs(figure):
    q = deque([])
    points = {}
    for i in range(6):
        for j in range(6):
            if figure[i][j] == 1:
                start = [i , j]
                break
    q.append(start)
    points[tuple(start)] = ((0 , 0 , 1),(1 , 0 , 0),(0 , 1 , 0))
    visited = set()
    visited.add((start[0],start[1]))
    faces = set()
    faces.add((0 , 0 , 1))
    while q:
        x , y = q.popleft()
        a , b , c = points[(x , y)]
        for dx , dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= 6 or ny < 0 or ny >= 6:continue
            if figure[nx][ny] == 0:continue
            if (nx , ny) in visited:continue
            q.append([nx , ny])
            visited.add((nx , ny))
            if dx == -1 and dy == 0:
                na = b
                nb = (-a[0],-a[1],-a[2])
                nc = c
            elif dx == 1 and dy == 0:
                na = (-b[0],-b[1],-b[2])
                nb = a
                nc = c
            elif dx == 0 and dy == -1:
                na = c
                nb = b
                nc = (-a[0],-a[1],-a[2])
            elif dx == 0 and dy == 1:
                na = (-c[0],-c[1],-c[2])
                nb = b
                nc = a
            points[(nx , ny)] = (na , nb , nc)
            if na in faces:return
            faces.add(na)
    return True

def main():
    c = int(input())
    for i in range(c):
        blank_line = input()
        figure = [list(map(int , input().split())) for a in range(6)]
        if bfs(figure):
            print("correct")
        else:
            print("incorrect")
        if i != c-1:print()
if __name__ == "__main__":
    main()

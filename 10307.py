from collections import deque

class DSU:
    def __init__(self , n):
        self.size = [1]*n
        self.parent = list(range(n))
    def find(self , x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self , a , b):
        roota , rootb = self.find(a) , self.find(b)

        if roota != rootb:

            if self.size[roota] < self.size[rootb]:
                roota , rootb = rootb , roota

            self.size[roota] += self.size[rootb]
            self.parent[rootb] = roota

            return True

        return False

def kruskal(p , dist):


    dist = list(set(dist))
    dist = sorted(dist , key = lambda x : x[2])
    ans = 0
    v = p - 1

    dsu = DSU(p)

    for a , b , d in dist:
        if dsu.union(a , b):
            ans += d
            v -= 1 
        if v <= 0:
            return ans

    return None




def bfs(n , m , arr , ps , x , y , _index):
    
    directions = ((-1,0),(1,0),(0,-1),(0,1))
    q = deque([])
    check = [[False]*m for _ in range(n)]
    q.append([x , y , 0])
    check[x][y] = True
    d = []
    ans = 1
    start = _index[(x , y)]

    while q:
        x , y , count = q.popleft()

        for dx , dy in directions:
            nx , ny = x + dx , y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if arr[nx][ny] == '#':continue
            if check[nx][ny]:continue
            if arr[nx][ny] == 'A' or arr[nx][ny] == 'S':
                d.append((start , _index[(nx , ny)] , count+1))
                ans += 1
                if ans >= len(ps):
                    return d
            q.append([nx , ny , count + 1])
            check[nx][ny] = True

    return None

def main():

    test = int(input())

    for case in range(test):

        m , n = map(int , input().split())
        arr = []
        ps = set()
        _index = {}

        for i in range(n):
            line = input()
            arr.append([])

            for j in range(m):
                if line[j] == 'A' or line[j] == 'S':
                    _index[(i , j)] = len(ps)
                    ps.add((i , j))
                arr[-1].append(line[j])
        
        dist = []
        for x , y in ps:
            dist += bfs(n , m , arr , ps , x , y , _index)

        ans = kruskal(len(ps) , dist)
        print(ans)

if __name__ == "__main__":
    main()

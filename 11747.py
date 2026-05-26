class DSU:
    def __init__(self , n):
        self.parents = list(range(n))
        self.size = [1]*n
    def find(self , x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self , a , b):
        roota , rootb = self.find(a) , self.find(b)
        if roota != rootb:
            if self.size[roota] < self.size[rootb]:
                roota , rootb = rootb , roota
            self.parents[rootb] = roota
            self.size[roota] += self.size[rootb]
            return True
        return False

def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        lines = []
        for i in range(m):
            u , v , w = map(int , input().split())
            lines.append([w , u , v])
        lines = sorted(lines)
        dsu = DSU(n)
        ans = []
        for w , u , v in lines:
            if not dsu.union(u , v):
                ans.append(w)
        if len(ans) != 0:
            print(' '.join(map(str , sorted(ans))))
        else:
            print('forest')

if __name__ == "__main__":
    main()

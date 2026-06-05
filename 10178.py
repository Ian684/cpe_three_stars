class DSU:
    def __init__(self , n):
        self.parents = list(range(n))
        self.size = [1]*n
    def find(self , x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self , a , b):
        roota , rootb = self.find(a) , self.find(b)
        if roota != rootb:
            if self.size[roota] < self.size[rootb]:
                roota , rootb = rootb , roota
            self.size[roota] += self.size[rootb]
            self.parents[rootb] = roota
            return True
        return False

def main():
    while True:
        try:
            n , e = map(int , input().split())
            c = 1
            check = {}
            dsu = DSU(n)
            idx = 0
            for i in range(e):
                a , b = input().split()
                if a not in check:
                    check[a] = idx
                    idx += 1
                if b not in check:
                    check[b] = idx
                    idx += 1
                if not dsu.union(check[a] , check[b]):
                    c += 1
            print(c)
        except EOFError:break

if __name__ == "__main__":
    main()

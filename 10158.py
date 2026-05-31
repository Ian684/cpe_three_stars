class DSU:
    def __init__(self , n):
        self.n = n
        self.parents = list(range(2*n))
        self.size = [1]*(2*n)
    
    def find(self , x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self , a , b):
        roota , rootb = self.find(a) , self.find(b)
        if self.size[roota] < self.size[rootb]:
            roota , rootb = rootb , roota
        if roota != rootb:
            self.parents[rootb] = roota
            self.size[roota] += self.size[rootb]

    def setfriends(self , a , b):
        if a == b:return True
        if self.find(a) == self.find(b + self.n):
            return False
        self.union(a , b)
        self.union(a + self.n , b + self.n)
        return True
        
    def setenemies(self , a , b):
        if a == b:return False
        if self.find(a) == self.find(b):
            return False
        self.union(a + self.n , b)
        self.union(a , b + self.n)
        return True
        

def main():
    while True:
        try:
            n = int(input())
            dsu = DSU(n)
            while True:
                command , a , b = map(int , input().split())
                if command == 0 and a == 0 and b == 0:break
                if command == 1:
                    flag = dsu.setfriends(a , b)
                    if not flag:
                        print(-1)
                elif command == 2:
                    flag = dsu.setenemies(a , b)
                    if not flag:
                        print(-1)
                elif command == 3:
                    if a == b or dsu.find(a) == dsu.find(b):
                        print(1)
                    else:
                        print(0)
                elif command == 4:
                    if a != b and dsu.find(a) == dsu.find(b + n):
                        print(1)
                    else:
                        print(0)
        except EOFError:break

if __name__ == "__main__":
    main()

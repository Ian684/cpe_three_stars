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

def main():
    t = int(input())
    for c in range(t):
        blank_line = input()
        n = int(input())
        points = []
        for i in range(n):
            x , y = map(int , input().split())
            points.append([x , y])
        dsu = DSU(n)
        m = int(input())
        for i in range(m):
            a , b = map(int , input().split())
            dsu.union(a-1 , b-1)
        lines = []
        for i in range(n):
            for j in range(i+1,n):
                x1 , y1 = points[i]
                x2 , y2 = points[j]
                w = (x1-x2)**2 + (y1-y2)**2
                lines.append([w , i , j])
        lines = sorted(lines)
        ans = []
        for w , i , j in lines:
            if dsu.find(i) == dsu.find(j):continue
            dsu.union(i , j)
            ans.append([i , j])
        if len(ans) == 0:
            print("No new highways need")
        else:
            for i in range(len(ans)):
                print(ans[i][0]+1 , ans[i][1]+1)
        if c != t-1:print()

if __name__ == "__main__":
    main()

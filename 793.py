import sys
sys.setrecursionlimit(200000)
size = []
parent = {}
n = None

def find(a):
    global size , parent , n
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a , b):
    global size , parent , n
    roota , rootb = find(a) , find(b)
    if roota != rootb:
        if size[roota] < size[rootb]:
            roota , rootb = rootb , roota
        parent[rootb] = roota
        size[roota] += size[rootb]

def main():
    global size , parent , n
    n = int(input())
    line = input()
    for i in range(n):
        point = int(input())
        operate = []
        size = [1]*point
        for j in range(point):
            parent[j] = j
        while True:
            try:
                line = input()
                if line == "":break
            except EOFError:break
            p , a , b = line.split()
            operate.append([p , int(a)-1 , int(b)-1])
        success = 0
        unsuccess = 0
        for p , a , b in operate:
            if p == "c":
                union(a , b)
            else:
                if find(a) == find(b):
                    success += 1
                else:
                    unsuccess += 1
        print(f"{success},{unsuccess}")
        if i != n - 1:
            print()
if __name__ == "__main__":
    main()

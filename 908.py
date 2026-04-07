parent = {}
size = {}

def find(a):
    global parent
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a , b):
    global parent , size
    roota , rootb = find(a) , find(b)
    if roota != rootb:
        if size[roota] < size[rootb]:
            roota , rootb = rootb , roota
        parent[rootb] = roota
        size[roota] += size[rootb]
        return True
    return False

def main():
    global parent , size
    first = True
    while True:
        try:
            line = input()
            if line == "":continue
        except EOFError:break
        n = int(line)
        old = 0
        for i in range(n-1):
            a , b , w = map(int , input().split())
            old += w
        k = int(input())
        lines = []
        for i in range(k):
            a , b , w = map(int , input().split())
            lines.append([w , a , b])
        m = int(input())
        for i in range(m):
            a , b , w = map(int , input().split())
            lines.append([w , a , b])
        lines = sorted(lines)
        ans = 0
        c = 0
        parent = {}
        size = {}
        for i in range(1 , n+1):
            parent[i] = i
            size[i] = 1
        for w , a , b in lines:
            if union(a , b):
                ans += w
                c += 1
            if c == n-1:break
        if first:
            first = False
        else:
            print()
        print(old)
        print(ans)
if __name__ == "__main__":
    main()

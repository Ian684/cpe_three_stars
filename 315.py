from collections import deque
def bfs(check , lines , n , i , start):
    q = deque([start])
    while q:
        point = q.popleft()
        for l in lines[point]:
            if l == i:continue
            if check[l]:continue
            check[l] = True
            q.append(l)
    return check
def main():
    while True:
        n = int(input())
        if n == 0:break
        lines = {}
        for i in range(n):
            lines[i] = []
        while True:
            line = input()
            if line == '0':break
            line = list(map(int , line.split()))
            for l in line[1:]:
                lines[line[0]-1].append(l-1)
                lines[l-1].append(line[0]-1)
        original_tree = 0
        check = [False]*n
        for j in range(n):
            if check[j]:continue
            check[j] = True
            check = bfs(check , lines , n , -1 , j)
            original_tree += 1
        c = 0
        for i in range(n):
            check = [False]*n
            check[i] = True
            tree = 0
            for j in range(n):
                if check[j]:continue
                check[j] = True
                check = bfs(check , lines , n , i , j)
                tree += 1
            if tree != original_tree:
                c += 1
        print(c)
if __name__ == "__main__":
    main()

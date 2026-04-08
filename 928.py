from collections import deque
ans = None
n , m = None , None
arr = []
check = []
start , end = None , None
def bfs():
    global arr , n , m , check , ans , start , end
    q = deque([start+[1 , 0]])
    while q:
        x , y , step , count = q.popleft()
        next_step = step+1
        if next_step == 4:
            next_step = 1
        if x-step >= 0 and len(check[x-step][y]) != 3:
            flag = True
            for dx in range(1 , step):
                if len(check[x-dx][y]) == 3:
                    flag = False
                    break
            if flag:
                if [x-step , y] == end:
                    ans = count+1
                    return
                check[x-step][y].add(next_step) 
                q.append([x-step , y , next_step , count+1])
        if x+step < n and len(check[x+step][y]) != 3:
            flag = True
            for dx in range(1 , step):
                if len(check[x+dx][y]) == 3:
                    flag = False
                    break
            if flag:
                if [x+step , y] == end:
                    ans = count+1
                    return
                check[x+step][y].add(next_step) 
                q.append([x+step , y , next_step , count+1])
        if y-step >= 0 and len(check[x][y-step]) != 3:
            flag = True
            for dy in range(1 , step):
                if len(check[x][y-dy]) == 3:
                    flag = False
                    break
            if flag:
                if [x , y-step] == end:
                    ans = count+1
                    return
                check[x][y-step].add(next_step) 
                q.append([x , y-step , next_step , count+1])
        if y+step < m and len(check[x][y+step]) != 3:
            flag = True
            for dy in range(1 , step):
                if len(check[x][y+dy]) == 3:
                    flag = False
                    break
            if flag:
                if [x , y+step] == end:
                    ans = count+1
                    return
                check[x][y+step].add(next_step) 
                q.append([x , y+step , next_step , count+1])
    ans = "NO"
    return 
def main():
    global arr , n , m , check , ans , start , end
    test = int(input())
    for _ in range(test):
        n , m = map(int , input().split())
        arr = []
        check = [[set() for j in range(m)] for i in range(n)]
        for i in range(n):
            arr.append(input())
            for j in range(m):
                if arr[i][j] == "#":
                    check[i][j] = set([1,2,3])
                elif arr[i][j] == "S":
                    start = [i , j]
                elif arr[i][j] == "E":
                    end = [i , j]
        ans = 0
        bfs()
        print(ans)
if __name__ == "__main__":
    main()

weight , height = [] , []
arr = []
count = []
w , h , n = None , None , None
ans = 0

def judge(x , y , a , b):
    global h , w , arr
    if x + a > h or y + b > w:
        return False
    for i in range(a):
        for j in range(b):
            if arr[x+i][y+j]:
                return False
    return True

def set(x , y , a , b , d):
    global arr
    for i in range(a):
        for j in range(b):
            arr[x+i][y+j] = d

def dfs(x , y):
    global weight , height , arr , w , h , n , ans , count
    if y >= w:
        x += 1
        y = 0
    if x >= h:
        ans += 1
        return
    if arr[x][y]:
        dfs(x , y+1)
    else:
        for i in range(n):
            if count[i]:
                if judge(x , y , height[i] , weight[i]):
                    set(x , y , height[i] , weight[i] , 1)
                    count[i] -= 1
                    dfs(x , y+1)
                    set(x , y , height[i] , weight[i] , 0)
                    count[i] += 1
                if judge(x , y , weight[i] , height[i]) and weight[i] != height[i]:
                    set(x , y , weight[i] , height[i] , 1)
                    count[i] -= 1
                    dfs(x , y+1)
                    set(x , y , weight[i] , height[i] , 0)
                    count[i] += 1
                    
def main():
    global weight , height , arr , w , h , n , ans , count
    while True:
        try:
            line = input()
            if line == "":continue
            w , h , n = map(int , line.split())
            weight = [0]*n
            height = [0]*n
            count = [0]*n
            arr = [[0]*w for _ in range(h)]
            c = 0
            for i in range(n):
                a , b , c = map(int , input().split())
                count[i] = a
                height[i] = b
                weight[i] = c
        except EOFError:break
        dfs(0 , 0)
        print(ans)
if __name__ == "__main__":
    main()

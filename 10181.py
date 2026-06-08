from heapq import *

def get_h(block):
    
    count = 0
    for i in range(16):
        if block[i] == 0:continue

        num = block[i]
        nx , ny = i//4 , i%4

        j = num - 1
        mx , my = j//4 , j%4

        count += abs(nx - mx) + abs(ny - my)

    return count

def inversion(block):
    
    count = 0

    for i in range(16):
        if block[i] == 0:continue
        for j in range(i+1 , 16):
            if block[j] == 0:continue
            if block[i] > block[j]:
                count += 1
    zero = block.index(0)
    row_from_bottom = 4 - zero//4

    if row_from_bottom + count & 1:
        return True
    return False

def bfs(arr):
    q = []
    heapify(q)
    aim = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    aim = tuple(aim)
    i = arr.index(0)
    startx = i//4
    starty = i%4
    arr = tuple(arr)
    heappush(q , [get_h(arr) , startx , starty , 0 , arr , ""])
    check = set()
    check.add(arr)
    directions = ((-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R'))

    while q:
        distance , x , y , step , block , path = heappop(q)

        if step > 50:continue
        if aim == block:return path
        now = x*4+y
        for dx , dy , d in directions:
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:continue
            _next = nx*4+ny
            new_block = list(block)
            new_block[now] , new_block[_next] = new_block[_next] , new_block[now]
            new_block = tuple(new_block)
            if new_block in check:continue
            
            check.add(new_block)
            new_step = step + 1
            new_distance = new_step + get_h(new_block)
            heappush(q , [new_distance , nx , ny , new_step , new_block , path + d])


    return None
def main():
    t = int(input())
    for c in range(t):
        temp = []
        for i in range(4):
            temp += list(map(int , input().split()))
        if not inversion(temp):
            print("This puzzle is not solvable.")
            continue
        ans = bfs(temp)
        if ans is None:
            print("This puzzle is not solvable.")
        else:
            print(ans)

if __name__ == "__main__":
    main()

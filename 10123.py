import sys
sys.setrecursionlimit(2000)

def remove_blocks(blocks , i , left ,right):
    position , weight = blocks[i]
    new_left , new_right = left , right

    new_left -= (position+1.5)*weight
    new_right -= (position-1.5)*weight

    return new_left , new_right

def valid(blocks , i , left , right):
    position , weight = blocks[i]
    if left - (position+1.5)*weight < 0:
        return False
    if right - (position-1.5)*weight > 0:
        return False
    return True

def cal_original(l , w , n , blocks):

    left , right = 0 , 0
    
    left += 1.5*w
    for i in range(n):
        position , weight = blocks[i]
        left += (position+1.5)*weight

    if left < 0:
        return None , None


    right += -1.5*w
    for i in range(n):
        position , weight = blocks[i]
        right += (position-1.5)*weight

    if right > 0:
        return None , None

    return left , right

def solve(l , w , n , blocks):
    
    left , right = cal_original(l , w , n , blocks)
    if left is None and right is None:
        return None

    blocks = sorted(blocks , key = lambda x : -abs(x[0] * x[1]))

    check = [False]*n
    ans = []
    history = set()

    def dfs(count , buf):
        nonlocal left , right , check , ans , history
        if buf in history:
            return False
        if count <= 0:
            return True
        for i in range(n):
            if check[i]:continue
            if valid(blocks , i , left , right):
                temp = [left , right]
                left , right , = remove_blocks(blocks , i , left , right)
                check[i] = True
                if dfs(count - 1 , buf^(1 << i)):
                    ans.append(blocks[i])
                    return True
                check[i] = False
                left , right = temp[0] , temp[1]
        
        history.add(buf)
        return False

    buf = (1 << n) - 1
    if not dfs(n , buf):
        return None
    return ans[::-1]


def main():
    now = 0
    while True:
        try:
            l , w , n = map(int , input().split())
            if l == 0 and w == 0 and n == 0:break
            blocks = []
            for i in range(n):
                position , weight = map(int , input().split())
                blocks.append([position , weight])

        except EOFError:break
        ans = solve(l , w , n , blocks)
        print(f"Case {now+1}:")
        now += 1
        if ans is None:
            print("Impossible")
        else:
            for position , weight in ans:
                print(position , weight)

if __name__ == "__main__":
    main()

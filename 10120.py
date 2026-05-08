from collections import deque

def bfs(n , m):
    q = deque([])
    q.append([1 , 3])
    check = set()
    check.add((1 , 3))

    while q:
        position , step = q.popleft()
        
        next_step = step + 2
        left = position - step
        right = position + step

        if left == m or right == m:
            return True

        if left >= 0 and (left , next_step) not in check:
            check.add((left , next_step))
            q.append([left , next_step])
        if right <= n and (right , next_step) not in check:
            check.add((right , next_step))
            q.append([right , next_step])

    return False

def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        if n >= 49:
            print("Let me try!")
            continue
        if bfs(n , m):
            print("Let me try!")
        else:
            print("Don't make fun of me!")

if __name__ == "__main__":
    main()

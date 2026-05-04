from collections import deque

def bfs(n , lines , n1 , n2 , n3):
    if n1 == n3 or n2 == n3:return 0
    q = deque([])
    q.append([n1 , n2 , 0])
    check = set()
    check.add((n1 , n2))
    check.add((n2 , n1))

    while q:
        first , second , steps = q.popleft()
        
        if (first , second) in lines:
            for _next in lines[(first , second)]:
                if (second , _next) in check:continue
                if _next == n3:return steps+1
                check.add((second , _next))
                check.add((_next , second))
                q.append([second , _next , steps+1])

        if (second , first) in lines:
            for _next in lines[(second , first)]:
                if (first , _next) in check:continue
                if _next == n3:return steps+1
                check.add((first , _next))
                check.add((_next , first))
                q.append([first , _next , steps+1])

    return None

def main():
    now = 0
    while True:
        n = int(input())
        if n == 0:break
        lines = {}
        for i in range(1 , n+1):
            temp = list(map(int , input().split()))
            for j in range(1 , n+1):
                if temp[j-1] == 0:continue
                if (i , j) not in lines:
                    lines[(i , j)] = []
                lines[(i , j)].append(temp[j-1])
        n1 , n2 , n3 = map(int , input().split())
        ans = bfs(n , lines , n1 , n2 , n3)
        print(f"Game #{now+1}")
        now += 1
        if ans is None:
            print("Destination is Not Reachable !")
        else:
            print(f"Minimum Number of Moves = {ans}")
        print()
if __name__ == "__main__":
    main()

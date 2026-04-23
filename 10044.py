from collections import deque
n , m = None , None
lines = {}
levels = {}

def bfs():
    global lines , levels , n , m
    if "Erdos, P." not in lines:return 
    q = deque([])
    q.append("Erdos, P.")
    while q:
        name = q.popleft()
        for _next in lines[name]:
            if _next in levels:continue
            levels[_next] = levels[name] + 1
            q.append(_next)
    return 

def main():
    global lines , levels , n , m
    c = int(input())
    for _ in range(c):
        try:
            n , m = map(int , input().split())
            lines = {}
            for i in range(n):
                line = input().split(":")[0]
                line = line.split(',')
                for a in range(0 , len(line)-1 , 2):
                    name1 = line[a].strip() + ', ' + line[a+1].strip()
                    for b in range(0 , len(line)-1 , 2):
                        name2 = line[b].strip() + ', ' + line[b+1].strip()
                        if name1 == name2:continue
                        if name1 not in lines:
                            lines[name1] = set()
                        if name2 not in lines:
                            lines[name2] = set()
                        lines[name1].add(name2)
                        lines[name2].add(name1)
            levels = {}
            levels["Erdos, P."] = 0
            bfs()
            print(f"Scenario {_+1}")
            for i in range(m):
                aim = input().strip()
                if aim in levels:
                    print(f"{aim} {levels[aim]}")
                else:
                    print(f"{aim} infinity")
        except EOFError:break
if __name__ == "__main__":
    main()

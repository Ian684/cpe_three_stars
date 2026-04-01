# use tarjan algorithm
dfn = []
low = []
check = []
is_cut = []
timer = 0
def generate_low(n , lines , u , parent):
    global dfn , low , check , timer , is_cut
    dfn[u] = timer
    low[u] = timer
    timer += 1
    check[u] = True
    children = 0
    for v in lines[u]:
        if not check[v]:
            children += 1
            generate_low(n , lines , v , u)
            low[u] = min(low[u] , low[v])
            if parent != -1 and low[v] >= dfn[u]:
                is_cut[u] = True
        elif check[v] and v != parent:
            low[u] = min(low[u] , dfn[v])
    if parent == -1 and children > 1:
        is_cut[u] = True
def main():
    global dfn , low , check , timer , is_cut
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
        timer = 0
        dfn = [0]*n
        low = [0]*n
        check = [False]*n
        is_cut = [False]*n
        for st in range(n):
            if check[st]:continue
            generate_low(n , lines , st , -1)
        print(sum(is_cut))
if __name__ == "__main__":
    main()

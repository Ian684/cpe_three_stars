def euler(n , m):

    if n < 10 and m < 10:return ""

    lines = [[0]*10 for i in range(10)]
    in_out = [0]*10

    for i in range(n , m+1):
        if i < 10:continue
        a , b = i // 10 , i % 10
        lines[a][b] += 1
        in_out[a] += 1
        in_out[b] -= 1
    
    in_p = []
    out_p = []

    for i in range(10):
        if in_out[i] > 0:
            out_p += [i]*in_out[i]
        elif in_out[i] < 0:
            in_p += [i]*-in_out[i]

    while len(in_p) > 1 and len(out_p) > 1:
        lines[in_p.pop()][out_p.pop()] += 1

    if out_p:
        start = out_p[0]
    else:
        for i in range(10):
            if any(lines[i]):
                start = i
                break

    path = ""
    def dfs(u):
        nonlocal path
        for v in range(10):
            while lines[u][v] > 0:
                lines[u][v] -= 1
                dfs(v)
        path += str(u)

    dfs(start)
    path = path[::-1]

    return path

def main():
    while True:
        try:
            n , m = map(int , input().split())
        except EOFError:break
        ans = euler(n , m)
        for i in range(n , min(m , 9) + 1):
            if str(i) not in ans:
                ans += str(i)
        print(ans)

if __name__ == "__main__":
    main()

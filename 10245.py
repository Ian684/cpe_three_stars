from math import *

def dis(a , b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def merge(a , b):
    
    merged = []
    i , j = 0 , 0

    while i < len(a) and j < len(b):
        if a[i][1] <= b[j][1]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    
    merged += a[i:]
    merged += b[j:]
    return merged

def solve(now):

    if len(now) == 1:
        return 1 << 32 , now
    elif len(now) == 2:
        return dis(now[0] , now[1]) , now if now[0][1] <= now[1][1] else now[::-1]
    
    mid = len(now)//2
    left , right = now[:mid] , now[mid:]

    l , ly = solve(left)
    r , ry = solve(right)
    d = min(l , r)
    merged = merge(ly , ry)

    xmid = (left[-1][0]+right[0][0]) / 2
    _next = []

    for i in range(len(merged)):
        if abs(merged[i][0] - xmid) >= d:continue
        _next.append(merged[i])
    
    for i in range(len(_next)):
        for j in range(i+1 , i+8):
            if j >= len(_next):break
            if _next[j][1] - _next[i][1] >= d:break
            d = min(d , dis(_next[j] , _next[i]))

    return d , merged

def main():
    while True:
        n = int(input())
        if n == 0:break
        ps = []
        for _ in range(n):
            ps.append(list(map(float , input().split())))
        ans , total = solve(sorted(ps))
        if ans >= 10000:
            print("INFINITY")
        else:
            print(f"{ans:.4f}")

if __name__ == "__main__":
    main()

from math import *
cards = []
envelopes = []
ans = []

def check(p, q, A, B):
    if (p <= A and q <= B) or (p <= B and q <= A):
        return True
    
    diag = sqrt(p*p + q*q)
    alpha = atan2(q, p)
    
    h , w = A , B
    if h < diag:
        try:
            theta = alpha + acos(h / diag)
            if 0 <= theta <= 1.57079632679:
                width_required = p * sin(theta) + q * cos(theta)
                if width_required <= w + 1e-9:
                    return True
        except (ValueError, ZeroDivisionError):pass
    return False

def dfs(cur , money , result):
    global cards , envelopes , ans
    if cur >= len(cards):
        if money < ans[0]:
            ans = [money]+result
        return
    if money > ans[0]:return
    ch , cw = cards[cur]
    for i in range(len(envelopes)):
        if i in result:continue
        eh , ew , p = envelopes[i]
        if check(ch , cw , eh , ew) or check(cw , ch , eh , ew):
            dfs(cur+1 , money+p , result+[i])
            continue
    return

def main():
    global cards , envelopes , ans
    now = 0
    first = True
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        cards = []
        envelopes = []
        for i in range(n):
            cards.append(list(map(int , input().split())))
        for i in range(m):
            envelopes.append(list(map(int , input().split())))
        ans = [1 << 60]
        money = 0
        cur = 0
        result = []
        dfs(cur , money , result)
        if first:first = False
        else:print()
        print(f"Case #{now+1}")
        now += 1
        if ans[0] == 1 << 60:
            print("cannot buy")
            continue
        for a in ans[1:]:
            print(a+1)
if __name__ == "__main__":
    main()

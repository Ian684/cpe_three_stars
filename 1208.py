from heapq import *
check = []
lines = {}
n = None
ans = []
def prim():
    global check , lines , n , ans
    q = []
    heapify(q)
    for l , score in lines[0]:
        heappush(q , [score , 0 , l])
    c = 1
    check[0] = True
    while True:
        p , x , y = heappop(q)
        if check[y]:continue
        check[y] = True
        c += 1
        ans.append([p , min(x , y) , max(x , y)])
        if c >= n:return
        for l , score in lines[y]:
            if check[l]:continue
            heappush(q , [score , y , l])
    return

def main():
    global check , lines , n , ans
    c = int(input())
    for i in range(c):
        n = int(input())
        lines = {}
        for j in range(n):
            line = list(map(int ,input().split(", ")))
            for k in range(j+1 , n):
                if line[k] == 0:continue
                if j not in lines:
                    lines[j] = []
                if k not in lines:
                    lines[k] = []
                lines[j].append([k , line[k]])
                lines[k].append([j , line[k]])
        check = [False]*n
        ans = []
        prim()
        print(f"Case {i+1}:")
        for point , start , end in sorted(ans):
            print(f"{chr(65+start)}-{chr(65+end)} {point}")
if __name__ == "__main__":
    main()

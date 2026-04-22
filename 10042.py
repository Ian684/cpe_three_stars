from math import *

def generate():
    limit = int(sqrt(10**9)) + 10
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit))+1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False
    
    prime = []
    for k , v in enumerate(seive):
        if v:
            prime.append(k)

    return prime

def main():
    prime = generate()
    c = int(input())
    for _ in range(c):
        n = int(input()) 
        i = n+1
        if i < 2:
            i = 2
        while True:
            count = 0
            t = i
            temp = t
            while temp > 0:
                count += temp % 10
                temp //= 10
            arr = {}
            for p in prime:
                if t == 1:
                    break
                while t % p == 0:
                    t //= p
                    if p not in arr:
                        arr[p] = 0
                    arr[p] += 1
            if t != 1:
                if t not in arr:
                    arr[t] = 0
                arr[t] += 1
            total = 0
            for k , v in arr.items():
                total += v
                temp = k
                while temp > 0:
                    count -= (temp % 10)*v
                    temp //= 10
            if total != 1:
                if count == 0:
                    print(i)
                    break
            i += 1
if __name__ == "__main__":
    main()

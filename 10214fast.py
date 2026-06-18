# 類似埃式篩法
limit = 2010
prime = []
mu = [None]*limit
visited = [False]*limit
def mobius():
    mu[1] = 1
    for i in range(2 , limit):
        if not visited[i]:
            prime.append(i)
            mu[i] = -1
            visited[i] = True
        for p in prime:
            if p * i >= limit:break
            visited[i*p] = True
            if i % p == 0:
                mu[i*p] = 0
                break
            mu[i*p] = -mu[i]
    # for i in range(2 , limit):
    #     mu[i] += mu[i-1]
    return 

def main():
    mobius()
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:break
        N = (2*a+1)*(2*b+1)-1
        if a > b:
            a , b = b , a
        K = 0
        for d in range(1 , a+1):
            K += mu[d]*(a//d)*(b//d)
        # 分塊加速，預處理前綴
        # i = 1
        # while True:
        #    if i >= a+1:break
        #    j = min(a//(a//i) , b//(b//i))
        #    K += (mu[j] - mu[i-1])*(a//i)*(b//i)
        #    i = j+1
        K = 4*K+4
        print(f"{K/N:.7f}")

if __name__ == "__main__":
    main()

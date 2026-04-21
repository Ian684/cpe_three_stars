import sys

def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    c = int(next(tokens))
    for cc in range(c):
        n = int(next(tokens))
        k = int(next(tokens))
        arr = []
        for i in range(n):
            arr.append(int(next(tokens)))
        dp = [set() for _ in range(n)]
        dp[0].add(arr[0]%k)
        dp[0].add(-arr[0]%k)
        for i in range(1 , n):
            for last in dp[i-1]:
                temp = (last+arr[i])%k
                if temp not in dp[i]:
                    dp[i].add(temp)
                temp = (last-arr[i])%k
                if temp not in dp[i]:
                    dp[i].add(temp)
        for last in dp[n-1]:
            if last == 0:
                print("Divisible")
                break
        else:
            print("Not divisible")
if __name__ == "__main__":
    main()

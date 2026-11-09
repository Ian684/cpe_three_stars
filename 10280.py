def main():

    test = int(input())

    for case in range(test):

        line = input()
        w , n = map(int , input().split())
        w *= 1000
        arr = set()
        result = 1 << 32

        for i in range(n):
            mn , mx = map(int , input().split())
            
            for i in range(mn , mx+1):
                arr.add(i)

            temp = mn*mn/(mx - mn)
            result = min(result , temp)

        if w >= result:
            print(0)

        else:
            dp = [0]*(w+1)
            for i in arr:
                for j in range(i , w+1):
                    dp[j] = max(dp[j] , dp[j-i] + i)
            
            print(w - dp[w])

        if case != test - 1:print()

if __name__ == "__main__":
    main()

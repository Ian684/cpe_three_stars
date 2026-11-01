def main():

    test = int(input())
    for case in range(test):

        line = input()
        w = int(input())*100
        ncar = 0
        arr = [0]
        prev = [0]
        now = 0

        while True:
            line = input()
            if line == '':continue
            n = int(line)
            if n == 0:break
            arr.append(n)
            now += n
            prev.append(now)
            ncar += 1
    
        dp = [[False]*(w+1) for _ in range(ncar+1)]
        dp[0][0] = True
        choice = [[-1]*(w+1) for _ in range(ncar+1)]

        ans = [0 , 0]
        for i in range(ncar):
            for j in range(w + 1):
                if not dp[i][j]:continue
                if j + arr[i+1] <= w:
                    dp[i + 1][j + arr[i+1]] = True
                    choice[i + 1][j + arr[i+1]] = 0
                    ans = [i + 1 , j + arr[i+1]]
                if prev[i] - j + arr[i+1] <= w:
                    dp[i + 1][j] = True
                    choice[i + 1][j] = 1
                    ans = [i + 1 , j]

        result = []
        j = ans[1]
        for i in range(ans[0] , 0 , -1):
            if choice[i][j] == 0:
                result.append("port")
                j -= arr[i]
            elif choice[i][j] == 1:
                result.append("starboard")
        print(ans[0])
        for a in result[::-1]:
            print(a)
        if case != test - 1:print()

if __name__ == "__main__":
    main()

import sys

def main():
    input_data = sys.stdin.readlines()
    idx = 0
    t = int(input_data[idx].strip())
    idx += 1
    for _ in range(t):
        while idx < len(input_data) and input_data[idx].strip() == "":
            idx += 1
        aim = int(input_data[idx].strip())
        idx += 1
        arr = [[0 , 0]]
        while idx < len(input_data):
            line = input_data[idx].strip()
            idx += 1
            if line == "":
                break
            a , b = map(int , line.split())
            if a > aim:continue
            arr.append([a , b])
        arr.append([aim , 0])
        n = len(arr)
        dp = [[1 << 60]*201 for i in range(n)]
        dp[0][100] = 0
        if 100 - arr[1][0] >= 0:
            dp[1][100-arr[1][0]] = 0
        for i in range(1 , n-1):
            pos1 , price1 = arr[i]
            pos2 , price2 = arr[i+1]
            w = pos2 - pos1
            for j in range(201):
                if dp[i][j] == 1 << 60:
                    continue
                for k in range(201-j):
                    if j - w + k >= 0:
                        dp[i+1][j-w+k] = min(dp[i+1][j-w+k] , dp[i][j] + k*price1)

        ans = min(dp[-1][100:])
        if ans == 1 << 60:
            print("Impossible")
        else:
            print(ans)
        if _ != t - 1:
            print()
if __name__ == "__main__":
    main()

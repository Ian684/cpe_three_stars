def main():
    ans = [0 , 1]
    now = 2
    for i in range(2 , 51):
        temp = i
        if temp & 1:
            temp += 1
        ans.append(ans[i-1]+temp)
    test = int(input())
    for i in range(test):
        print(ans[int(input())])

if __name__ == "__main__":
    main()

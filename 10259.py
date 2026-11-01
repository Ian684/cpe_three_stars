def main():
    test = int(input())
    for case in range(test):
        line = input()
        n , k = map(int , input().split())
        arr = []
        for i in range(n):
            arr.append(list(map(int , input().split())))
        ans = dfs(n , k , arr)
        print(ans)
        if case != test - 1:print()

if __name__ == "__main__":
    main()

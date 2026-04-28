def main():
    c = int(input())
    for _ in range(c):
        x = input()
        z = input()
        now = 0
        ans = 0
        def solve(x , z , now):
            nonlocal ans
            if now >= len(z):
                ans += 1
                return
            for s in range(len(x)):
                if x[s] == z[now]:
                    solve(x[s+1:] , z , now+1)
            return
        solve(x , z , now)
        print(ans)
if __name__ == "__main__":
    main()

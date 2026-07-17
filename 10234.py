def main():
    while True:
        try:
            s = input().lower()
            t = int(input())
            for _ in range(t):
                n = int(input())
                count = {}
                for i in range(len(s)-n+1):
                    temp = s[i:i+n]
                    if temp not in count:
                        count[temp] = 0
                    count[temp] += 1
                ans = sorted(count.items() , key = lambda x : (-x[1] , x[0]))[0]
                print(ans[1] , ans[0])

        except EOFError:break
if __name__ == "__main__":
    main()

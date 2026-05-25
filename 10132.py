def main():
    t = int(input())
    blank_line = input()
    for _ in range(t):
        binarys = {}
        l = 0
        count = 0
        while True:
            try:
                line = input()
                if line == "":break
                if len(line) not in binarys:
                    binarys[len(line)] = []
                binarys[len(line)].append(line)
                l += len(line)
                count += 1
            except EOFError:break
        l //= (count//2)
        check = {}
        for i in range(1 , l//2+1):
            j = l-i
            if i not in binarys or j not in binarys:continue
            if i == j:
                for a in range(len(binarys[i])):
                    for b in range(len(binarys[i])):
                        if a == b:continue
                        s1 , s2 = binarys[i][a] , binarys[i][b]
                        aim = s1 + s2
                        if aim not in check:
                            check[aim] = 0
                        check[aim] += 1
            else:
                for s1 in binarys[i]:
                    for s2 in binarys[j]:
                        aim = s1 + s2
                        if aim not in check:
                            check[aim] = 0
                        check[aim] += 1
                        aim = s2 + s1
                        if aim not in check:
                            check[aim] = 0
                        check[aim] += 1
        print(sorted(check.items() , key = lambda x : -x[1])[0][0])
        if _ != t - 1:print()

if __name__ == "__main__":
    main()

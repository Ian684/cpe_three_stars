def main():
    while True:
        arr = {}
        flag = True
        for i in range(0 , 256):
            arr[i] = [set(),[]]
        try:
            while True:
                line = input().split()
                for l in line:
                    if l == "()":break
                    value , position = l[1:-1].split(",")
                    if position in arr[len(position)][0]:
                        flag = False
                    arr[len(position)][0].add(position)
                    arr[len(position)][1].append([position , value])
                if line[-1] == "()":break
        except EOFError:break
        if len(arr[0][1]) == 0:
            flag = False
        if flag:
            for i in range(2 , 256):
                for a in arr[i][0]:
                    if a[:-1] not in arr[i-1][0]:
                        flag = False
                        break
                if not flag:break
        if flag:
            first = True
            for i in range(0 , 256):
                for a in sorted(arr[i][1]):
                    if first:
                        first = False
                        print(a[1] , end="")
                        continue
                    print(f" {a[1]}" , end="")
            print()
        else:
            print("not complete")

if __name__ == "__main__":
    main()

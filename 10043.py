def main():
    c = int(input())
    for _ in range(c):
        n , m = map(int , input().split())
        trees = []
        y_coords = set()
        while True:
            try:
                line = input()
                if line == "0":break
                line = list(map(int , line.split()))
                if len(line) == 3:
                    trees.append([line[1] , line[2]])
                    y_coords.add(line[2])
                elif len(line) == 5:
                    for k in range(line[0]):
                        trees.append([line[1]+k*line[3] , line[2]+k*line[4]])
                        y_coords.add(line[2]+k*line[4])
            except EOFError:break
        for y in y_coords:
            trees.append([0 , y])
            trees.append([n , y])
        trees = sorted(trees)
        ans = -1
        for i in range(len(trees)):
            upper , lower = m , 0
            x1 , y1 = trees[i]
            for j in range(i+1 , len(trees)):
                x2 , y2 = trees[j]
                ans = max(ans , abs((x2-x1)*(upper - lower)))
                if y1 == y2:
                    upper = lower
                    break
                if y2 > y1:
                    upper = min(upper , y2)
                elif y2 < y1:
                    lower = max(lower , y2)
        y_coords = [0] + sorted(list(y_coords)) + [m]
        for i in range(len(y_coords)-1):
            ans = max(ans , n*(y_coords[i+1]-y_coords[i]))
        print(ans)
if __name__ == "__main__":
    main()

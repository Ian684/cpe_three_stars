import sys
sys.setrecursionlimit(5000)
aim = None
replaces = {}
result = set()

def dfs(now_str):
    global aim , replaces , result
    result.add(now_str)
    if len(result) > 1000:
        return False
    if len(now_str) == 0:return True
    for a in range(len(now_str)):
        for b in range(a+1 , len(now_str)+1):
            if now_str[a:b] not in replaces:continue
            for k in replaces[now_str[a:b]]:
                y = now_str[:a] + k + now_str[b:]
                if y in result:
                    continue
                if not dfs(y):
                    return False
    return True
def main():
    global aim , replaces , result
    c = int(input())
    blank_line = input()
    for i in range(c):
        aim = input()[1:-1]
        replaces = {}
        while True:
            try:
                line = input()
                if line == "":
                    break
                a , b = line.split("->")
                a , b = a[1:-1] , b[1:-1]
                if a not in replaces:
                    replaces[a] = []
                replaces[a].append(b)
            except EOFError:break
        result = set()
        if not dfs(aim):
            print("Too many.")
        else:
            print(len(result))
        if i != c - 1:print()
if __name__ == "__main__":
    main()

from collections import deque

def bfs(start , end , dictionary):
    q = deque([])
    q.append([start , []])
    check = set()
    check.add(start)
    alph = set()
    for i in range(26):
        alph.add(chr(i+97))

    while q:
        now , change = q.popleft()
        
        for al in alph:
            for i in range(len(now)):
                temp = now[:i] + al + now[i+1:]
                if temp in check:continue
                if temp not in dictionary:continue
                if temp == end:
                    return change+[i , al]
                check.add(temp)
                q.append([temp , change+[i , al]])
    return None


def main():
    dictionary = set()
    while True:
        line = input()
        if line == "":break
        dictionary.add(line)
    first = True
    while True:
        try:
            start , end = input().split()
        except EOFError:break
        ans = bfs(start , end , dictionary)
        if first:first = False
        else:print()
        if ans is None:
            print("No solution.")
        else:
            print(start)
            for i in range(0 , len(ans) , 2):
                pos , al = ans[i] , ans[i+1]
                start = start[:pos] + al + start[pos+1:]
                print(start)

if __name__ == "__main__":
    main()

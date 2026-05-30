import sys
sys.setrecursionlimit(20000)

def solve(commands1 , goto1 , commands2 , goto2):

    def is_goto_loop(commands, goto, pos):
        seen = set()
        while "goto" in commands[pos] and "if" not in commands[pos]:
            if pos in seen:
                return True
            seen.add(pos)
            n = int(commands[pos].split("goto")[1])
            pos = goto[n]
        return False

    check = set()
    def dfs(pos1 , pos2):
        nonlocal check
        loop1 = is_goto_loop(commands1, goto1, pos1)
        loop2 = is_goto_loop(commands2, goto2, pos2)

        if loop1 or loop2:
            return loop1 and loop2

        if (pos1 , pos2) in check:
            return True

        check.add((pos1 , pos2))
        c1 , c2 = commands1[pos1] , commands2[pos2]
        if c1 == "stop" and c2 == "stop":
            return True
        elif c1 == "stop" and "goto" not in c2:
            return False
        elif c2 == "stop" and "goto" not in c1:
            return False
        if "goto" in c1 and "goto" in c2:
            if "if" in c1 and "if" in c2:
                c1 , c2 = c1.split("goto") , c2.split("goto")
                if c1[0] != c2[0]:
                    return False
                n1 , n2 = int(c1[1]) , int(c2[1])
                if dfs(goto1[n1] , goto2[n2]) and dfs(pos1+1 , pos2+1):
                    return True
            elif "if" in c1:
                n2 = int(c2.split("goto")[1])
                if dfs(pos1 , goto2[n2]):
                    return True
            elif "if" in c2:
                n1 = int(c1.split("goto")[1])
                if dfs(goto1[n1] , pos2):
                    return True
            else:
                c1 , c2 = c1.split("goto") , c2.split("goto")
                n1 , n2 = int(c1[1]) , int(c2[1])
                if dfs(goto1[n1] , goto2[n2]):
                    return True
        elif "goto" in c1 and "if" not in c1:
            n1 = int(c1.split("goto")[1])
            if dfs(goto1[n1] , pos2):
                return True
        elif "goto" in c2 and "if" not in c2:
            n2 = int(c2.split("goto")[1])
            if dfs(pos1 , goto2[n2]):
                return True
        else:
            if c1 != c2:
                return False
            if dfs(pos1+1 , pos2+1):
                return True
        return False

    if dfs(0 , 0):
        return True
    return False

def parse_line(line, goto, i):
    temp = ""
    if len(line) >= 6:
        num = line[:5].strip()
        if (num == "" or num.isdigit()) and line[5].isspace():
            if num != "":
                goto[int(num)] = i
            statement = line[6:]
        else:
            parts = line.strip().split(maxsplit=1)

            if len(parts) == 2 and parts[0].isdigit():
                goto[int(parts[0])] = i
                statement = parts[1]
            else:
                statement = line.strip()
    else:
        statement = line.strip()
    for x in statement.split():
        temp += x.strip()
    return temp

def main():
    data = sys.stdin.read().splitlines()
    programs = []
    commands = []
    goto = {}
    i = 0
    for line in data:
        if line.strip() == "":
            continue
        temp = parse_line(line, goto, i)
        commands.append(temp)
        i += 1
        if temp == "stop":
            programs.append((commands, goto))
            commands = []
            goto = {}
            i = 0
    for k in range(0, len(programs), 2):
        commands1, goto1 = programs[k]
        commands2, goto2 = programs[k + 1]
        if solve(commands1, goto1, commands2, goto2):
            print("The programs are equivalent.")
        else:
            print("The programs are not equivalent.")
if __name__ == "__main__":
    main()

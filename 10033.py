def main():
    c = int(input())
    blank_line = input()
    for _ in range(c):
        commands = ["000"]*1000
        i = 0
        while True:
            try:
                line = input()
                if line == "":break
                commands[i] = line
                i += 1
            except EOFError:break
        count = 0
        now = 0
        registers = [0]*10
        while True:
            command = commands[now]
            count += 1
            if command == "100":break
            ins , d , s = int(command[0]) , int(command[1]) , int(command[2])
            if ins == 0:
                if registers[s] != 0:
                    now = registers[d]
                    continue
            elif ins == 2:
                registers[d] = s
            elif ins == 3:
                registers[d] += s
                registers[d] %= 1000
            elif ins == 4:
                registers[d] *= s
                registers[d] %= 1000
            elif ins == 5:
                registers[d] = registers[s]
            elif ins == 6:
                registers[d] += registers[s]
                registers[d] %= 1000
            elif ins == 7:
                registers[d] *= registers[s]
                registers[d] %= 1000
            elif ins == 8:
                registers[d] = int(commands[registers[s]])
            elif ins == 9:
                commands[registers[s]] = str(registers[d]).zfill(3)
            now += 1
        print(count)
        if _ != c-1:print()
if __name__ == "__main__":
    main()

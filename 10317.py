def solve(plus , minus , nums):

    if sum(nums) & 1:
        return None , None
    a = []
    b = []
    target = sum(nums) // 2

    def dfs(now , count , plus):
        nonlocal a , b , target

        if now >= len(nums):
            if count == target and plus == 0:
                return True
            return False

        if plus > len(nums) - now:
            return False

        if count > target:
            return False

        if plus > 0:
            a.append(nums[now])
            if dfs(now + 1 , count + nums[now] , plus - 1):
                return True
            a.pop()

        b.append(nums[now])
        if dfs(now + 1 , count , plus):
            return True
        b.pop()
        
        
        return False

    if dfs(0 , 0 , plus):
        return a , b

    return None , None

def main():
    while True:
        try:
            line = input().split()
        except EOFError:break

        plus , minus = 1 , 1
        i = 0
        flag = False
        nums = []
        while i < len(line):
            if line[i] == '=':flag = True
            elif line[i] == '+':
                if flag:
                    minus += 1
                else:
                    plus += 1
            elif line[i] == '-':
                if flag:
                    plus += 1
                else:
                    minus += 1
            else:
                temp = abs(int(line[i]))
                nums.append(temp)
            i += 1
            
        plus , minus = solve(plus , minus , nums)

        if plus is None and minus is None:
            print("no solution")
        else:
            i = 0
            flag = True
            while i < len(line):
                if line[i] == '=':
                    print(' = ' , end="")
                    i += 1
                    break
                elif line[i] == '+':
                    print(' + ' , end="")
                    flag = True
                elif line[i] == '-':
                    print(' - ' , end="")
                    flag = False
                else:
                    if flag:
                        print(plus.pop() , end="")
                    else:
                        print(minus.pop() , end="")
                i += 1
            flag = True
            while i < len(line):
                if line[i] == '+':
                    print(' + ' , end="")
                    flag = True
                elif line[i] == '-':
                    print(' - ' , end="")
                    flag = False
                else:
                    if flag:
                        print(minus.pop() , end="")
                    else:
                        print(plus.pop() , end="")
                i += 1
            print()

if __name__ == "__main__":
    main()

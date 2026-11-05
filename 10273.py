from math import *

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        cows = []
        cycle = 1
        for i in range(n):
            c = list(map(int , input().split()))
            cycle = lcm(cycle , c[0])
            cows.append(c[1:])
        choice = set(range(n))
        day = 0
        final_day = -1
        while True:
            flag = False
            for i in range(cycle):
                m = 1 << 32
                choose = -1
                find = False
                for cow in choice:
                    l = len(cows[cow])
                    if cows[cow][day%l] < m:
                        m = cows[cow][day%l]
                        choose = cow
                        find = True
                    elif cows[cow][day%l] == m:
                        find = False
                if find:
                    final_day = day
                    flag = True
                    choice.remove(choose)
                day += 1
            if not flag:break

        print(len(choice) , final_day+1)

if __name__ == "__main__":
    main()

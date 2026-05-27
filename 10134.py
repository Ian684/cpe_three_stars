def main():
    t = int(input())
    blank_line = input()
    for c in range(t):
        bait = 0
        fish = 0
        last_fish_time = 0
        now_time = 0
        count_fish_time = 0
        first = True
        while True:
            try:
                ins = input()
                if ins == "":break
                if ins == "lunch":
                    now_time += 10
                elif ins == "bait":
                    now_time += 10
                    if bait < 3:
                        bait += 0.5
                elif ins == "fish":
                    if bait >= 1:
                        if first:
                            first = False
                            fish += 1
                            last_fish_time = now_time
                            bait -= 1
                            count_fish_time = 0
                        else:
                            count_fish_time += 1
                            if count_fish_time >= 3 and now_time - last_fish_time >= 70:
                                bait -= 1
                                fish += 1
                                count_fish_time = 0
                                last_fish_time = now_time
                    now_time += 10
            except EOFError:break
        print(fish)
        if c != t-1:print()

if __name__ == "__main__":
    main()

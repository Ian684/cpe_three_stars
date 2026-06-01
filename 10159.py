def main():
    alph = [[4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14] , [15 , 16 , 17 ,18 , 19 , 20 , 21 , 22 , 23] , [24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32] , [33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43] , [0 , 2 , 1 , 8 , 7 , 17 , 16 , 25 , 24 , 34 , 33] , [3 , 10 , 9 , 19 , 18 , 27 , 26 , 36 , 35] , [12 , 11 , 21 , 20 , 29 , 28 , 38 , 37 , 44] , [14 , 13 , 23 , 22 , 31 , 30 , 40 , 39 , 46 , 45 , 47] , [4 , 5 , 15 , 16 , 25 , 26 , 36 , 37 , 44 , 45 , 47] , [6 , 7 , 17 , 18 , 27 , 28 , 38 , 39 , 46] , [1 , 8 , 9 , 19 , 20 , 29 , 30 , 40 , 41] , [0 , 2 , 3 , 10 , 11 , 21 , 22 , 31 , 32 , 42 , 43]]

    cells_to_lines = {}
    for i in range(len(alph)):
        temp = alph[i]
        for t in temp:
            if t not in cells_to_lines:
                cells_to_lines[t] = []
            cells_to_lines[t].append(i)

    while True:
        try:
            line = list(map(int , input().split()))
        except EOFError:break
        arr = [1 << 60]*48
        for al in range(12):
            aim = line[al]
            temp = alph[al]
            for _next in temp:
                arr[_next] = min(arr[_next] , aim)
        valid = True
        for al in range(12):
            aim = line[al]
            temp = alph[al]
            flag = False
            for _next in temp:
                if arr[_next] == aim:
                    flag = True
                    break
            if not flag:
                valid = False
                break
        if valid:
            big = sum(arr)
        else:
            print("NO SOLUTION")
            continue

        dp = {0:0}
        for i in range(48):
            next_dp = {}
            max_value = arr[i]

            for v in range(max_value+1):
                achieve_mask = 0
                for l_idx in cells_to_lines[i]:
                    if line[l_idx] == v:
                        achieve_mask |= (1 << l_idx)

                for state , old_v in dp.items():
                    new_state = state | achieve_mask
                    new_value = old_v + v
                    if new_state not in next_dp or new_value < next_dp[new_state]:
                        next_dp[new_state] = new_value
            dp = next_dp
        target_state = 2**12-1
        if target_state in dp:
            small = dp[target_state]
            print(small , big)
        else:
            print("NO SOLUTION")
if __name__ == "__main__":
    main()

import sys

def solve():
    sys.setrecursionlimit(5000)
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    case_num = 1
    
    while ptr < len(input_data):
        L_raw = int(input_data[ptr])
        W_board = int(input_data[ptr+1])
        N = int(input_data[ptr+2])
        ptr += 3
        if L_raw == 0 and W_board == 0 and N == 0: break
        
        blocks = []
        for _ in range(N):
            p = int(input_data[ptr])
            w = int(input_data[ptr+1])
            blocks.append((p, w))
            ptr += 2

        blocks.sort(key=lambda x: abs(x[0] * x[1]), reverse=True)
        pre_L = []
        pre_R = []
        init_L = 3 * W_board
        init_R = -3 * W_board
        
        for p, w in blocks:
            lp = (2 * p + 3) * w
            rp = (2 * p - 3) * w
            pre_L.append(lp)
            pre_R.append(rp)
            init_L += lp
            init_R += rp
        
        print(f"Case {case_num}:")
        case_num += 1
        
        if init_L < 0 or init_R > 0:
            print("Impossible")
            continue
            
        memo = set()
        ans = []
        
        pre_L = tuple(pre_L)
        pre_R = tuple(pre_R)
        
        def dfs(mask, cur_L, cur_R):
            if mask == 0:
                return True
            if mask in memo:
                return False
            
            for i in range(N):
                if (mask >> i) & 1:
                    next_L = cur_L - pre_L[i]
                    next_R = cur_R - pre_R[i]
                    
                    if next_L >= 0 and next_R <= 0:
                        if dfs(mask ^ (1 << i), next_L, next_R):
                            ans.append(blocks[i])
                            return True
            
            memo.add(mask)
            return False

        if dfs((1 << N) - 1, init_L, init_R):
            for p, w in reversed(ans):
                print(f"{p} {w}")
        else:
            print("Impossible")

if __name__ == "__main__":
    solve()

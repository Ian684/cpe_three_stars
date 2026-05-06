import sys
from fractions import Fraction

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    first = True
    
    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
            if n == 0:
                break
            
            unknown = int(next(iterator))
            equation = int(next(iterator))
            
            matrix = []
            for _ in range(equation):
                row = []
                for _ in range(unknown + 1):
                    val_str = next(iterator)
                    row.append(Fraction(val_str))
                matrix.append(row)
                
            row_idx = 0
            col_idx = 0
            
            while row_idx < equation and col_idx < unknown:
                pivot_row = row_idx
                for i in range(row_idx, equation):
                    if matrix[i][col_idx] != 0:
                        pivot_row = i
                        break
                
                if matrix[pivot_row][col_idx] == 0:
                    col_idx += 1
                    continue
                    
                matrix[row_idx], matrix[pivot_row] = matrix[pivot_row], matrix[row_idx]
                
                pivot_val = matrix[row_idx][col_idx]
                for j in range(col_idx, unknown + 1):
                    matrix[row_idx][j] /= pivot_val
                    
                for i in range(equation):
                    if i != row_idx:
                        factor = matrix[i][col_idx]
                        if factor != 0:
                            for j in range(col_idx, unknown + 1):
                                matrix[i][j] -= factor * matrix[row_idx][j]
                                
                row_idx += 1
                col_idx += 1
            rank_A = 0
            rank_aug = 0
            
            for i in range(equation):
                is_zero_A = True
                for j in range(unknown):
                    if matrix[i][j] != 0:
                        is_zero_A = False
                        break
                        
                is_zero_aug = is_zero_A and (matrix[i][unknown] == 0)
                
                if not is_zero_A:
                    rank_A += 1
                if not is_zero_aug:
                    rank_aug += 1
                    
            if not first:
                print()
            first = False
            
            print(f"Solution for Matrix System # {n}")
            
            if rank_A < rank_aug:
                print("No Solution.")
            elif rank_A < unknown:
                constants = unknown - rank_A
                print(f"Infinitely many solutions containing {constants} arbitrary constants.")
            else:
                for i in range(unknown):
                    ans = matrix[i][unknown]
                    if ans.denominator == 1:
                        print(f"x[{i+1}] = {ans.numerator}")
                    else:
                        print(f"x[{i+1}] = {ans.numerator}/{ans.denominator}")
                        
        except StopIteration:
            break

if __name__ == "__main__":
    solve()

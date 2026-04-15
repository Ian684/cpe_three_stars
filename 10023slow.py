import sys

def binary_sqrt():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    c = int(next(tokens))
    for _ in range(c):
        n = int(next(tokens))
        digit = (len(str(n)) + 1) // 2
        left = 10**(digit-1)
        right = 10**(digit)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == n:
                ans = mid
                break
            elif sq < n:
                left = mid + 1
            else:
                right = mid - 1
        print(ans)
if __name__ == "__main__":
    result = binary_sqrt()

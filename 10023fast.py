import sys

def main():
        input_data = sys.stdin.read().split()
        tokens = iter(input_data)
        c = int(next(tokens))
        for _ in range(c):
            num = int(next(tokens))
            x = 1 << ((num.bit_length() + 1) // 2)
            while True:
                new_x = (x + int(num) // x) // 2
                if new_x >= x:
                    print(x)
                    if _ != c - 1:
                        print()
                    break
                x = new_x
if __name__ == "__main__":
    main()

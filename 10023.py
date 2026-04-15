from decimal import Decimal , getcontext
import sys

def main():
        input_data = sys.stdin.read().split()
        tokens = iter(input_data)
        c = int(next(tokens))
        getcontext().prec = 500
        for _ in range(c):
            print(int(Decimal(next(tokens)).sqrt()))
            if _ != c - 1:
                print()
if __name__ == "__main__":
    main()

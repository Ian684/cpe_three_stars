def main():
    while True:
            num = int(input())
            if num == 0:break
            result = -1
            i = 1
            while i <= num:
                    q = num // i
                    j = num // q
                    result += q * ((i+j)*(j-i+1)//2)
                    i = j + 1
            print(result)
if __name__ == "__main__":
    main()

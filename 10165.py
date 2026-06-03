def main():
    while True:
        n = int(input())
        if n == 0:break
        nim_sum = 0
        for i in list(map(int , input().split())):
            nim_sum ^= i
        if nim_sum != 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()

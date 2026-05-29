def main():
    check = ["((A0|B0)|(A0|B0))"]
    for i in range(1 , 101):
        a = str(i)
        temp = "((A"+a+"|B"+a+")|("+check[i-1]+"|((A"+a+"|A"+a+")|(B"+a+"|B"+a+"))))"
        check.append(temp)

    t = int(input())
    for c in range(t):
        blank_line = input()
        print(check[int(input())-1])
        if c != t - 1:print()

if __name__ == "__main__":
    main()

def main():
    fab = [0 , 1 , 1]
    i = 3
    while True:
        fab.append(fab[i-1]+fab[i-2])
        if len(str(fab[-1])) > 1000:break
        i += 1   
        
    while True:
        try:
            n = int(input())
        except EOFError:break
        print(fab[n])

if __name__ == "__main__":
    main()

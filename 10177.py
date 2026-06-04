def main():
    s2 = [0]
    s3 = [0]
    s4 = [0]
    r2 = [0]
    r3 = [0]
    r4 = [0]
    count = 0
    for i in range(1 , 101):
        temp2 = s2[i-1]+i**2 
        temp3 = s3[i-1]+i**3 
        temp4 = s4[i-1]+i**4
        count += i
        s2.append(temp2)
        s3.append(temp3)
        s4.append(temp4)
        r2.append(count**2-temp2) 
        r3.append(count**3-temp3) 
        r4.append(count**4-temp4) 

    while True:
        try:
            n = int(input())
        except EOFError:break
        print(s2[n] , r2[n] , s3[n] , r3[n] , s4[n] , r4[n])

if __name__ == "__main__":
    main()

def C(n , k):

    temp = 1
    for j in range(n , max(k , n-k) , -1):
        temp *= j
    for j in range(min(k , n-k) , 0 , -1):
        temp /= j
    temp = int(temp)
    
    return temp


def main():

    c31 = []
    for i in range(31):
        temp = C(31 , i)
        c31.append(temp)

    while True:
        try:
            n = int(input())
        except EOFError:break
        if n == 0:
            print(0)
            continue
        if n == 2147483647:
            print(2147483647)
            continue
        ones = None
        temp = n
        for i in range(31):
            temp -= c31[i]
            if temp < 0:
                temp += c31[i]
                ones = i
                break
        count = set()
        remain = 32
        while True:
            if ones <= 0:break
            for i in range(ones , remain):
                left = C(i , ones)
                if left > temp:
                    remain = i
                    count.add(i)
                    break
            temp -= C(remain-1 , ones)
            ones -= 1
        ans = ''
        for i in range(1 , 32):
            if i not in count:
                ans = '0' + ans
            else:
                ans = '1' + ans
        ans = int(ans , 2)
        print(ans)


if __name__ == "__main__":
    main()

def solve(n , arr):
    
    l = len(arr)
    if l == 1:
        return [0]
    odd = []
    even = []
    for i in range(l):
        if arr[i] & 1:
            odd.append(i)
        else:
            even.append(i)
    
    new_arr = []
    temp = []
    for i in range(0 , len(odd)-1 , 2):
        pos1 = odd[i]
        pos2 = odd[i+1]
        value = (arr[pos1]+arr[pos2])//2
        temp.append([pos1 , pos2])
        new_arr.append(value)
    for i in range(0 , len(even)-1 , 2):
        pos1 = even[i]
        pos2 = even[i+1]
        value = (arr[pos1]+arr[pos2])//2
        temp.append([pos1 , pos2])
        new_arr.append(value)

    result = solve(n , new_arr)
    new_result = []
    for i in result:
        new_result.append(temp[i][0])
        new_result.append(temp[i][1])
    return new_result

def main():
    while True:
        n = int(input())
        if n == 0:break
        arr = list(map(int , input().split()))
        ans = solve(n , arr)
        for i in range(len(ans)):
            ans[i] = arr[ans[i]]
        print("Yes")
        print(' '.join(map(str , ans)))

if __name__ == "__main__":
    main()

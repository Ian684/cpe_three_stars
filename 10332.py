def solve(n , a , b , arr , his):

    ans = []

    def dfs(now , k):
        nonlocal a , b , ans , arr , his

        temp = []
        last = now[-1]
        for other in now[:-1]:
            if abs(last - other) not in his or his[abs(last - other)] <= 0:
                while temp:
                    his[temp.pop()] += 1
                return False
            his[abs(last - other)] -= 1
            temp.append(abs(last - other))
        if len(now) >= n:
            ans = now
            return True

        for i in range(k , -1 , -1):
            if his[arr[i]] > 0:
                aim = arr[i]
                l = i - 1
                break
        i , j = aim , b - aim
        if dfs(now + [i] , l):
            return True
        if dfs(now + [j] , l):
            return True
        while temp:
            his[temp.pop()] += 1
        return False

    if dfs([a , b] , len(arr)-1):
        return ans
    return None

def main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    p = 0

    while p < len(data):
        n = data[p]
        p += 1

        m = n * (n - 1) // 2
        arr = sorted(data[p:p + m])
        p += m

        a, b = 0, arr[-1]

        his = {}
        for x in arr:
            his[x] = his.get(x, 0) + 1

        ans = solve(n, a, b, arr, his)

        if ans is None:
            print("Incorrect Balance.")
        else:
            print(' '.join(map(str, sorted(ans))))

if __name__ == "__main__":
    main()

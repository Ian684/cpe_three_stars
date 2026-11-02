def generate_lps(p):

    lps = [0]*len(p)
    length = 0
    i = 1

    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1

    return lps

def candidates(aim):

    n = len(aim)
    lps = generate_lps(aim[::-1] + '#' + aim)
    k = lps[-1]

    result = [aim[::-1]]
    while k > 0:
        result.append(aim[:n-k][::-1])
        k = lps[k-1]
        
    return result


def main():
    while True:
        try:
            a = input()
            b = input()
        except EOFError:break
        ans = []
        for x in candidates(a):
            if b + x != (b + x)[::-1]:
                ans.append(x)
            else:
                for al in range(26):
                    if b + chr(97+al) + x != (b + chr(97+al) + x)[::-1] and a + chr(97+al) + x == (a + chr(97+al) + x)[::-1]:
                        ans.append(chr(97+al) + x)
                        break

        for x in candidates(b):
            if a + x != (a + x)[::-1]:
                ans.append(x)
            else:
                for al in range(26):
                    if b + chr(97+al) + x == (b + chr(97+al) + x)[::-1] and a + chr(97+al) + x != (a + chr(97+al) + x)[::-1]:
                        ans.append(chr(97+al) + x)
                        break

        ans = sorted(ans , key = lambda x : (len(x) , x))
        if len(ans) == 0:print("No solution.")
        else:print(ans[0])
            
if __name__ == "__main__":
    main()

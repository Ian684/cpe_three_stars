parents = {}
size = {}

def find(a):
    global parents , size
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a , b):
    global parents , size
    roota , rootb = find(a) , find(b)
    if roota != rootb:
        if size[roota] < size[rootb]:
            roota , rootb = rootb , roota
        parents[rootb] = roota
        size[roota] += size[rootb]

def valid(_in , _out):
    start = 0
    end = 0
    for x in range(26):
        if chr(97+x) not in _in:
            _in[chr(97+x)] = 0
        if chr(97+x) not in _out:
            _out[chr(97+x)] = 0
    for k , v in _in.items():
        if v != _out[k]:
            if v == _out[k] - 1:
                start += 1
            elif v == _out[k] + 1:
                end += 1
            else:
                return False
    if start == 1 and end == 1:
        return True
    if start == 0 and end == 0:
        return True
    return False

def valid2(arr):
    
    for x in arr:
        for y in arr:
            if x == y:continue
            if find(x) != find(y):return False
    return True

def init(a):
    global parents , size
    if a not in parents:
        parents[a] = a
    if a not in size:
        size[a] = 1

def main():
    global parents , size
    c = int(input())
    for i in range(c):
        parents = {}
        size = {}
        _in = {}
        _out = {}
        arr = set()
        n = int(input())
        for j in range(n):
            s = input()
            a , b = s[0] , s[-1]
            init(a)
            init(b)
            arr.add(a)
            arr.add(b)
            union(a , b)
            if a not in _out:
                _out[a] = 0
            if b not in _in:
                _in[b] = 0
            _out[a] += 1
            _in[b] += 1
        if valid(_in , _out):
            if valid2(arr):
                print("Ordering is possible.")
            else:
                print("The door cannot be opened.")
        else:
            print("The door cannot be opened.")

if __name__ == "__main__":
    main()

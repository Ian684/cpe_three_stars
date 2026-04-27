noun = set(['tom' , 'jerry' , 'goofy' , 'mickey' , 'jimmy' , 'dog' , 'cat' , 'mouse'])
verb = set(['hate' , 'hates' , 'love' , 'loves' , 'know' , 'knows' , 'like' , 'likes'])
article = set(['a' , 'the'])

def actor(line):
    if len(line) == 1 and line[0] in noun:
        return True
    if len(line) == 2 and line[0] in article and line[1] in noun:
        return True
    return False

def active_list(line):
    sp = [-1]
    for l in range(len(line)):
        if line[l] == 'and':
            sp.append(l)
    sp.append(len(line))
    flag = True
    for i in range(len(sp)-1):
        if not actor(line[sp[i]+1:sp[i+1]]):
            flag = False
            break
    if flag:
        return True
    return False

def action(line):
    for l in range(len(line)):
        if line[l] in verb:
            if active_list(line[:l]) and active_list(line[l+1:]):
                return True
            return False

def statement(line):
    sp = [-1]
    for l in range(len(line)):
        if line[l] == ',':
            sp.append(l)
    sp.append(len(line))
    flag = True
    for i in range(len(sp)-1):
        if not action(line[sp[i]+1:sp[i+1]]):
            flag = False
            break
    if flag:
        return True
    else:
        return False

def check(line):
    global noun , verb , article
    for l in line:
        if l not in noun and l not in verb and l not in article and l != ',' and l != 'and':return False
    if statement(line):
        return True
    return False

def main():
    while True:
        try:
            line = input().replace(',' , ' , ').split()
        except EOFError:break
        if check(line):
            print("YES I WILL")
        else:
            print("NO I WON'T")
if __name__ == "__main__":
    main()

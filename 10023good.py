from math import *
import sys

input_data = sys.stdin.read().split()
tokens = iter(input_data)
c = int(next(tokens))
for cc in range(c):
    n = next(tokens)
    arr = []
    if len(n) & 1:
        arr.append(int(n[0]))
        n = n[1:]
    for i in range(0 , len(n)-1 , 2): 
        arr.append(int(n[i:i+2]))
    div = int(sqrt(arr[0]))
    carry = arr[0]-div**2
    for i in range(1 , len(arr)):
        temp = carry*100+arr[i]
        x = 1
        while True:
            if x**2+20*x*div > temp:
                x -= 1
                break
            x += 1
        carry = temp - x**2 - 20*x*div
        div = div*10+x
    print(div)
    print()

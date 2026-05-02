from math import *

def main():
    n = int(input())
    eps = 1e-9
    for i in range(n):
        command , a , b , c = input().split()
        if command == "S":
            l , w , r = float(a) , float(b) , float(c)
            newr = r/sqrt(2)
            total = sqrt((l-2*newr)**2+(w-2*newr)**2)
            if total >= 2*newr and 2*newr <= w and 2*newr <= l:
                print(f"{total:.4f}")
            else:
                print("Not enough space for fission.")

        else:
            r1 , r2 , d = float(a) , float(b) , float(c)
            if r1 + r2 <= d:
                print(f"{1:.4f}")
                print("No compaction has occurred.")
            else:
                angle1 = acos((r2**2+d**2-r1**2)/(2*r2*d))
                big1 = (angle1)*(r2**2)
                angle2 = acos((r1**2+d**2-r2**2)/(2*r1*d))
                big2 = (angle2)*(r1**2)
    
                s = (r1+r2+d)/2
                remain = big1+big2-sqrt(s*(s-r1)*(s-r2)*(s-d))*2
                total = ((r1**2)*(pi) + (r2**2)*(pi))
                total = (total-remain)/total
                if total + eps >= 1:
                    print(f"{1:.4f}")
                    print("No compaction has occurred.")
                else:
                    print(f"{total:.4f}")
        print()
if __name__ == "__main__":
    main()

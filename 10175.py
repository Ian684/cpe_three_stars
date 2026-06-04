from math import *

def main():
    t = int(input())
    for _ in range(t):
        r1 , r2 , d , w , s = map(float , input().split())

        d1 = (r1**2-r2**2+d**2)/(2*d)
        d2 = d - d1
        h1 = r1 - d1
        h2 = r2 - d2

        surface = 4*pi*r1**2 + 4*pi*r2**2 - 2*r1*pi*h1 - 2*r2*pi*h2


        volume = (4/3)*pi*r1**3 + (4/3)*pi*r2**3 - pi*(((2/3)*r1**3-d1*r1**2+(1/3)*d1**3) + ((2/3)*r2**3-d2*r2**2+(1/3)*d2**3))

        
        print(f"{volume:.4f} {surface:.4f}")
        if w / volume < s:
            print("The Paired-Sphere Floats.")
        else:
            print("The Paired-Sphere Sinks.")

if __name__ == "__main__":
    main()

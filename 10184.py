from math import *

def dis(a):
    return sqrt((a[0])**2+(a[1])**2+(a[2])**2)

def dot(a , b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def main():
    radius = 6378
    locations = {}
    try:
        while True:
            line = input()
            if line == '#':break
            location , lat , lon = line.split()
            lat , lon = float(lat) , float(lon)
            lat , lon = lat/180*pi , lon/180*pi
            z = sin(lat)*radius
            x = cos(lat)*cos(lon)*radius
            y = cos(lat)*sin(lon)*radius
            locations[location] = [x , y , z]
        while True:
            line = input()
            if line == '#':break
            a , b , aim = line.split()
            if a not in locations or b not in locations or aim not in locations:
                print(f"{aim} is ? km off {a}/{b} equidistance.")
                continue
            al , bl , aiml = locations[a] , locations[b] , locations[aim]
            n = [al[0]-bl[0] , al[1]-bl[1] , al[2]-bl[2]]
            if dis(n) == 0:
                ans = 0
            else:
                angle = abs(dot(aiml , n))/(dis(aiml)*dis(n))
                angle = acos(min(1.0, max(0.0, angle)))
                angle = pi/2-angle
                ans = angle * radius
                ans = int(ans+0.5)
            print(f"{aim} is {ans} km off {a}/{b} equidistance.")
    except EOFError:return

if __name__ == "__main__":
    main()

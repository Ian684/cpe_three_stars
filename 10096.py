from math import *

def main():
    n = int(input())
    eps = 1e-9

    for i in range(n):
        command, a, b, c = input().split()

        if command == "S":
            l, w, r = float(a), float(b), float(c)
            newr = r / sqrt(2)

            total = sqrt((l - 2 * newr)**2 + (w - 2 * newr)**2)

            if total + eps >= 2 * newr and 2 * newr <= min(l, w) + eps:
                print(f"{total:.4f}")
            else:
                print("Not enough space for fission.")

        else:
            r1, r2, d = float(a), float(b), float(c)
            total = pi * (r1**2 + r2**2)

            if d >= r1 + r2:
                remain = 0

            elif d <= abs(r1 - r2):
                remain = pi * min(r1, r2)**2

            else:
                angle1 = acos(max(-1, min(1, (r2**2 + d**2 - r1**2) / (2 * r2 * d))))
                angle2 = acos(max(-1, min(1, (r1**2 + d**2 - r2**2) / (2 * r1 * d))))

                s = (r1 + r2 + d) / 2
                triangle = sqrt(max(0, s * (s-r1) * (s-r2) * (s-d)))

                remain = angle1 * r2**2 + angle2 * r1**2 - 2 * triangle

            ratio = (total - remain) / total
            ratio = min(1.0, max(0.0, ratio))

            print(f"{ratio:.4f}")

            if f"{ratio:.4f}" == "1.0000":
                print("No compaction has occurred.")

        print()

if __name__ == "__main__":
    main()

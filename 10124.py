import math

def main():
    while True:
        try:
            line = input().split()
            if not line: break
            d, m, a, j = map(float, line)
        except EOFError: break
        if m * j <= a**2:
            d_limit_m = m * math.sqrt(m / j)
            if d >= 2 * d_limit_m:
                ans = (d - 2 * d_limit_m) / m + 4 * math.sqrt(m / j)
            else:
                ans = 4 * (d / (2 * j))**(1/3)
        
        else:
            d_to_a = a**3 / j**2
            d_to_m = m**2 / a + m * a / j
            
            if d >= d_to_m:
                ans = (d - d_to_m) / m + 2 * (m / a + a / j)
            elif d >= d_to_a:
                v_peak = (-(a**2 / j) + math.sqrt((a**2 / j)**2 + 4 * a * d)) / 2
                ans = 2 * (v_peak / a + a / j)
            else:
                ans = 4 * (d / (2 * j))**(1/3)
        print(f"{ans:.1f}")

if __name__ == "__main__":
    main()

import math
import sys

def get_dist_to_slope_line(x, y, angle):
    if abs(math.cos(angle)) < 1e-12:
        return abs(x)
    m = math.tan(angle)
    return abs(m * x - y) / math.sqrt(m**2 + 1)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    ptr = 1
    for _ in range(n):
        rx, ry, r, x, y = map(float, input_data[ptr:ptr+5])
        ptr += 5
        
        d_house = math.hypot(x, y)
        d_tree = math.hypot(rx, ry)
        dist_to_line = abs(rx * y - ry * x) / d_house
        proj = (rx * x + ry * y) / d_house
        is_safe = (dist_to_line <= r) and (0 < proj < d_house)
        
        if not is_safe:
            print("0.000")
            continue
            
        r_angle = math.atan2(ry, rx)
        plus_angle = math.asin(r / d_tree)
        
        dist1 = get_dist_to_slope_line(x, y, r_angle + plus_angle)
        dist2 = get_dist_to_slope_line(x, y, r_angle - plus_angle)
        
        dist_to_tree_surface = math.hypot(x - rx, y - ry) - r
        
        result = min(dist1, dist2, dist_to_tree_surface)
        print(f"{max(0.0, result):.3f}")

if __name__ == "__main__":
    solve()

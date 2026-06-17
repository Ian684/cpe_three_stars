def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = n*(n-1)*(n-2)*(n-3)//24 + n*(n-1)//2 + 1
        print(ans)

if __name__ == "__main__":
    main()

# V - E + F = 1
# V => vertex
# E => line
# F => splited areas 

# we need to get F, so F = E - V + 1
# E = n + Cn2 + 2*Cn4 = outer line + inner line + some lines cross with others, so we need to add it (the graph below)
# V = n + Cn4 = original points + intersections

# if we randomly take four points, there must appear one intersection
# a----------d
# | \       /|
# |  \     / |
# |   \   /  |
# |    \ /   |
# |     \    |
# |    / \   |
# |   /   \  |
# |  /     \ | 
# | /       \|
# b----------c
# this add a point and two line

# so F = Cn4 + Cn2 + 1

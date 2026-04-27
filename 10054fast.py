import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t_cases = int(input_data[ptr])
    ptr += 1
    
    for i in range(1, t_cases + 1):
        n = int(input_data[ptr])
        ptr += 1
        
        adj = [[0] * 51 for _ in range(51)]
        degree = [0] * 51
        start_node = -1
        
        for _ in range(n):
            u = int(input_data[ptr])
            v = int(input_data[ptr+1])
            ptr += 2
            adj[u][v] += 1
            adj[v][u] += 1
            degree[u] += 1
            degree[v] += 1
        if i > 1:
            print()
        print(f"Case #{i}")
        
        possible = True
        for d in degree:
            if d % 2 != 0:
                possible = True
                possible = False
                break
        path = []
        if possible:
            stack = [start_node]
            vertices = []
            
            while stack:
                u = stack[-1]
                found_edge = False
                for v in range(1, 51):
                    if adj[u][v] > 0:
                        adj[u][v] -= 1
                        adj[v][u] -= 1
                        stack.append(v)
                        found_edge = True
                        break
                
                if not found_edge:
                    vertices.append(stack.pop())
            
            if len(vertices) != n + 1:
                possible = False
        
        if not possible:
            print("some beads may be lost")
        else:
            for j in range(len(vertices) - 1):
                print(f"{vertices[j]} {vertices[j+1]}")
if __name__ == "__main__":
    main()

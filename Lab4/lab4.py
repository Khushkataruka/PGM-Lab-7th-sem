import sys

def solve():
    if len(sys.argv) < 2:
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    if not lines:
        return
    
    n, m = map(int, lines[0].split())
    
    directed_adj = {i: [] for i in range(n)}
    undirected_adj = {i: [] for i in range(n)}
    
    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        directed_adj[u].append(v)
        undirected_adj[u].append(v)
        undirected_adj[v].append(u)
        
    descendants = {i: set([i]) for i in range(n)}
    for i in range(n):
        stack = [i]
        visited = set([i])
        while stack:
            curr = stack.pop()
            for nxt in directed_adj[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        descendants[i] = visited
        
    q_idx = m + 1
    q = int(lines[q_idx])
    
    for i in range(q_idx + 1, q_idx + 1 + q):
        parts = list(map(int, lines[i].split()))
        x = parts[0]
        y = parts[1]
        Z = set(parts[2:])
        
        all_trails_blocked = True
        stack = [[x]]
        
        while stack:
            path = stack.pop()
            curr = path[-1]
            
            if curr == y:
                is_trail_blocked = False
                for j in range(1, len(path) - 1):
                    prev = path[j-1]
                    w = path[j]
                    nxt = path[j+1]
                    
                    prev_to_w = w in directed_adj[prev]
                    w_to_nxt = nxt in directed_adj[w]
                    
                    if prev_to_w and not w_to_nxt:
                        if len(descendants[w].intersection(Z)) == 0:
                            is_trail_blocked = True
                            break
                    else:
                        if w in Z:
                            is_trail_blocked = True
                            break
                
                if not is_trail_blocked:
                    all_trails_blocked = False
                    break
                continue
                
            for neighbor in undirected_adj[curr]:
                if neighbor not in path:
                    stack.append(path + [neighbor])
                    
        if all_trails_blocked:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()

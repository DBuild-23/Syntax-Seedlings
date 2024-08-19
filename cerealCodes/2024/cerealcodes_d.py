# Credits by Saketh

def construct_grid(n, k):
    grid = [['0'] * n for _ in range(n)]
    
    full_rows = k // n  
    for i in range(full_rows):
        grid[i] = ['1'] * n
    
    remaining = k - (full_rows * n)
    if remaining > 0:
        grid[full_rows][:remaining] = ['1'] * remaining
    
    return [''.join(row) for row in grid]

n, k = map(int, input().split())

result = construct_grid(n, k)
for row in result:
    print(row)

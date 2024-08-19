#Credits by Saketh

def solve_case():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    flips_pattern1 = 0
    flips_pattern2 = 0
    
    for i in range(n):
        for j in range(m):
            expected1 = '1' if (i + j) % 2 == 0 else '0'
            expected2 = '0' if (i + j) % 2 == 0 else '1'
            
            if grid[i][j] != expected1:
                flips_pattern1 += 1
            if grid[i][j] != expected2:
                flips_pattern2 += 1
    
    return min(flips_pattern1, flips_pattern2)

t = int(input())
for _ in range(t):
    print(solve_case())

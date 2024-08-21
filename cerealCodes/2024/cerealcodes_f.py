# Credits to Saketh

from collections import defaultdict

def count_valid_pairs(n, a):
    diff_count = defaultdict(int)
    pair_count = 0
    
    for i, value in enumerate(a):
        diff = value - (i + 1)  
        pair_count += diff_count[diff]
        diff_count[diff] += 1
    
    return pair_count

n = int(input())
a = list(map(int, input().split()))

result = count_valid_pairs(n, a)
print(result)

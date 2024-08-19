// Credits by Daniel


value = {chr(i + 97): i for i in range(26)}  # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25


def reverse_char(c):
    val = value[c]
    rev_val = 25 - val
    return chr(rev_val + 97)


def opposite_char(c):
    val = value[c]
    opp_val = (val + 13) % 26
    return chr(opp_val + 97)


def min_moves_to_transform(n, s, t):
    moves = 0
    i = 0

    while i < n:
        if s[i] == t[i]:
            i += 1
            continue

        reverse_possible = reverse_char(s[i]) == t[i]
        opposite_possible = opposite_char(s[i]) == t[i]

        if not reverse_possible and not opposite_possible:
            return -1

        start = i
        while i < n and ((reverse_possible and reverse_char(s[i]) == t[i]) or
                         (opposite_possible and opposite_char(s[i]) == t[i])):
            i += 1

        moves += 1

    return moves


n = int(input())
s = input().strip()
t = input().strip()

result = min_moves_to_transform(n, s, t)
print(result)

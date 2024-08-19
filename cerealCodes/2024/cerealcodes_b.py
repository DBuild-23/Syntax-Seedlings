def is_simple_array(n, array):
    total_sum = sum(array)

    if total_sum % 2 != 0:
        return "NO"

    half_sum = total_sum // 2

    count_1 = array.count(1)
    count_2 = array.count(2)

    needed_from_2 = min(half_sum // 2, count_2)
    half_sum -= needed_from_2 * 2

    if half_sum <= count_1:
        return "YES"
    else:
        return "NO"


n = int(input())
array = list(map(int, input().split()))

print(is_simple_array(n, array))

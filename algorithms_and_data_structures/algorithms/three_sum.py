def find_sums_zero(nums: list):
    sollution = set()
    data = sorted(nums)
    i, j, k = 0, 1, len(nums) - 1
    while j < k:
        curent_value = data[i] + data[j] + data[k]
        if curent_value < 0:
            i += 1
            j += 1
        if curent_value > 0:
            k -= 1
        if curent_value == 0:
            sollution.add((i, j, k))
    return sollution


def find2sum(array: list, value: int) -> list:
    i, j = 0, len(array) - 1
    pairs = []
    while i < j:
        current_sum = array[i] + array[j]
        if current_sum > value:
            j -= 1
        if current_sum < value:
            i += 1
        if current_sum == value:
            pairs.append((array[i], array[j]))
            i += 1
            j -= 1
    return pairs


def find3sum(array: list) -> list:
    size = len(array)
    data = sorted(array)
    triples = set()
    for i in range(size-1):
        pairs = find2sum(data[i+1:], -data[i])
        for a, b in pairs:
            triples.add((data[i], a, b))
    return list(triples)


if __name__ == "__main__":
    result = find3sum([-1, 0, 1, 2, -1, -4])
    print(result)

if __name__ == "__main__":
    print(find_sums_zero([-1, 0, 1, 2, -1, -4]))
    print(find_sums_zero([]))
    print(find_sums_zero([0]))

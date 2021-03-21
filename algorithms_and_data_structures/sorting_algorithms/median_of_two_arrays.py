"""My sollution"""
def median_two_arrays(nums_a: list, nums_b: list) -> float:
    nums = sorted(nums_a + nums_b)
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    else:
        return (nums[(n//2)-1] + nums[n//2]) / 2


"""Better sollution"""
def merge(left: list, right: list) -> list:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    size1, size2 = len(left), len(right)
    i, j = 0, 0
    while i < size1 and j < size2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def median(left: list, right: list) -> float:
    data = merge(left, right)
    size = len(data)
    if size == 1:
        return data[0]
    if size % 2 == 1:
        return data[size // 2]
    l, r = (size - 1) // 2, (size + 1) // 2
    return (data[l] + data[r]) / 2.0


if __name__ == "__main__":
    a = [1, 2, 5]
    b = [3, 4]
    assert median(a, b) == 3

from typing import List, Optional


def binary_search(items: List[int], target: int) -> Optional[int]:
    left, right = 0, len(items) - 1
    while left <= right:
        middle = left + (right - left) // 2  # to samo co (right + left) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None

if __name__ == '__main__':
    data = list(range(12))
    print(data)
    # assert binary_search(data, 1001) is None
    # assert binary_search(data, 10) == 10
    print(binary_search(data, 8))

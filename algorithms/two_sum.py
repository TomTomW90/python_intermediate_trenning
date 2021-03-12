"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List, Tuple


def find_two_numbers_that_add(nums_list: list, target_sum: int) -> list:
    """My first sollution."""

    sollution = []
    for element in nums_list:
        wanted_element = target_sum - element
        try:
            element_index = nums_list.index(element)
            wanted_element_index = nums_list.index(wanted_element, element_index + 1)
            sollution = [element_index, wanted_element_index]
            break
        except ValueError:
            continue
    if not sollution:
        return 'Coditions can not be met.'
    return sollution


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """The best sollution."""

    i, j = 0, len(nums) - 1
    data = sorted(nums)
    while i < j:
        value = data[i] + data[j]
        if value > target:
            j -= 1
        if value < target:
            i += 1
        if value == target:
            break
    idx1 = nums.index(data[i])
    if data[i] == data[j]:
        idx2 = nums.index(data[j], idx1+1)
    else:
        idx2 = nums.index(data[j])
    return idx1, idx2


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))

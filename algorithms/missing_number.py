"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


def find_missing_number(nums_list: list) -> int:
    sollution = None
    for number in range(0, len(nums_list) + 1):
        if number not in nums_list:
            sollution = number
            break
    return sollution


def missing_number(nums: list) -> int:
    a_data = sorted(nums)
    b_data = range
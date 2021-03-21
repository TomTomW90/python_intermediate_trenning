"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


def find_missing_number(nums: list) -> int:
    nums.sort()
    n = 0
    while n == nums[n]:
        n += 1
        if n == len(nums):
            return nums[-1] + 1
    return nums[n] - 1


if __name__ == '__main__':
    list_of_nums = [3, 0, 1]
    print(find_missing_number(list_of_nums))

    list_of_nums = [0, 1]
    print(find_missing_number(list_of_nums))

    list_of_nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(find_missing_number(list_of_nums))

    list_of_nums = [0]
    print(find_missing_number(list_of_nums))

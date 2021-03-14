def median_two_arrays(nums_a: list, nums_b: list) -> float:
    nums = sorted(nums_a + nums_b)
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    else:
        return (nums[(n//2)-1] + nums[n//2]) / 2

if __name__ == "__main__":
    print(median_two_arrays([1, 3], [2]))
    print(median_two_arrays([1, 2], [3, 4]))
    print(median_two_arrays([0, 0], [0, 0]))
    print(median_two_arrays([], [1]))
    print(median_two_arrays([2], []))

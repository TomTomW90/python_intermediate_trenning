# def find_sums_zero(nums: list):
#     sollution = set()
#     data = sorted(nums)
#     i, j, k = 0, 1, len(nums) - 1
#     while j < k:
#         curent_value = data[i] + data[j] + data[k]
#         if curent_value < 0:
#             i += 1
#             j += 1
#         if curent_value > 0:
#             k -= 1
#         if curent_value == 0:
#             sollution.add((i, j, k))
#     return sollution


if __name__ == "__main__":
    print(find_sums_zero([-1, 0, 1, 2, -1, -4]))
    print(find_sums_zero([]))
    print(find_sums_zero([0]))

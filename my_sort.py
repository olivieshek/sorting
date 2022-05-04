def my_sort(nums: list) -> list:
    result = [0] * len(nums)
    for idx, n in enumerate(result):
        result[idx] = min(nums)
        nums.remove(min(nums))
    return result


print(my_sort([24, 28, 29, 26, 1, 22, 23, 6, 16, 27]))
def moveZeroes(nums: list) -> list:
    count = 0

    for i, num in enumerate(nums):
        if num == 0:
            count = count + 1
            continue

        nums[i], nums[i - count] = nums[i - count], nums[i]

    return nums

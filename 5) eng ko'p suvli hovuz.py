def maxArea(nums: list) -> int:
    i, j = 0, len(nums) - 1
    max_area = 0

    while i <= j:
        area = (j - i) * min(nums[i], nums[j])
        max_area = max(max_area, area)

        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1

    return max_area

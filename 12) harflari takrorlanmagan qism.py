def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    max_len = 0
    left = 0
    used_chars = set()

    for right in range(n):
        while s[right] in used_chars:
            used_chars.remove(s[left])
            left += 1
        used_chars.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

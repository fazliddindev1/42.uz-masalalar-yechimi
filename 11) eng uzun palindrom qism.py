def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return ""

    start, max_len = 0, 1

    for i in range(1, len(s)):
        low, high = i - 1, i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        low, high = i - 1, i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

    return s[start:start + max_len]

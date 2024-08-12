def longestCommonPrefix(words: list) -> str:
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        if not prefix:
            break

    return prefix

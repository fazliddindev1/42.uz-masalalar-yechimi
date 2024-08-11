def detectCapitalUse(word: str) -> bool:
    if word.isupper() or word.islower():
        return True

    return word[:1].isupper() and word[1:].islower()
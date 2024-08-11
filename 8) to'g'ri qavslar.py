OPEN = '('
CLOSE = ')'

def is_valid(s: str) -> bool:
    balance = 0

    for bracket in s:
        if bracket == OPEN:
            balance += 1
        elif bracket == CLOSE:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

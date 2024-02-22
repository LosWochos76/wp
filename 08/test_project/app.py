import math

def is_prime(number: int) -> bool:
    if number < 2:
        return False

    if number == 2:
        return True

    for divisor in range(2, int(math.sqrt(number))+1):
        if number % divisor == 0:
            return False

    return True

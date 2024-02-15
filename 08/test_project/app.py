def is_prime(number: int) -> bool:
    if number < 2:
        return False

    if number == 2:
        return True

    for divisor in range(3, int(number/2), 2):
        if number % divisor == 0:
            return False

    return True

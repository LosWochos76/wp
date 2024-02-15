"""This module collects some methods to show how to use pytest."""

def is_prime(number):
    '''Takes in a positive number and checks if it is a prime'''
    if number < 2:
        return False

    if number == 2:
        return True

    for divisor in range(3, int(number/2), 2):
        if number % divisor == 0:
            return False

    return True

import pytest
from test_project import app

def test_2():
    assert app.is_prime(2), "2 is a prime!"

def test_3():
    assert app.is_prime(3), "3 is a prime!"

def test_5():
    assert app.is_prime(5), "5 is a prime!"

def test_9():
    assert app.is_prime(9) is False, "9 is not a prime!"

def test_97():
    assert app.is_prime(97), "97 is a prime!"

def test_100():
    assert app.is_prime(100) is False, "100 is not a prime!"

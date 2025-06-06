"""Functions for simple calculations"""


def add(a: int, b: int) -> int:
    """Function for addition of two integers"""
    return a + b


def substract(a: int, b: int) -> int:
    """Function for substraction of two integers"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Function for multiplication of two integers"""
    return a * b


def divide(a: int, b: int) -> float:
    """Function for division of two integers"""
    if b == 0:
        return 0

    return a / b

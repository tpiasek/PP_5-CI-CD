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


def dec2bin(a: int) -> str:
    """Function for converting an integer to binary in range <0, 100>"""
    if a < 0 or a > 100:
        return "Range error!"

    result = ""

    while a > 0:
        result = str(a % 2) + result
        a //= 2

    return result

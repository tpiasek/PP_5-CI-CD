# Exemplary calculator tests

import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_substract(a, b, expected):
    result = utils.substract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8), (5, 0, 0)]
)
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, expected ",
    [
        (1, "1"),
        (3, "11"),
        (16, "10000"),
        (89, "1011001"),
        (100, "1100100"),
        (-2, "Range error!"),
        (101, "Range error!"),
        (200, "Range error!"),
    ],
)
def test_dec2bin(a, expected):
    result = utils.dec2bin(a)
    assert result == expected

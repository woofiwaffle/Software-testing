import pytest
from src.main import sum_of_numbers

@pytest.fixture
def numbers():
    return {
        1: 1,
        5: 15,
        10: 55,
        100: 5050,
        0: 0
    }

@pytest.mark.parametrize("input_num, expected_sum", [
    (1, 1),
    (5, 15),
    (10, 55),
    (100, 5050),
    (0, 0)
])
def test_sum_of_numbers(numbers, input_num, expected_sum):
    assert sum_of_numbers(input_num) == expected_sum

@pytest.mark.xfail
def test_sum_of_numbers_fail():
    assert sum_of_numbers(100) == 5051
@pytest.mark.mymark
def test_sum_of_numbers_custom():
    assert sum_of_numbers(2) == 3

from custom_program._SimpleProgram import calculate_sum
import pytest

@pytest.fixture
def get_input_list():
    return [1,2,3]

def test_calculate_sum():
    assert calculate_sum(1,2,3) == 6, "Should be 6"


def test_calculate_sum_with_fixtures(get_input_list):
    assert calculate_sum(*get_input_list) == 6, "Should be 6"


@pytest.mark.parametrize("input_list,excpected_result", [
    ([1,2], 3),
])
def test_calculate_sum_parameterized(input_list, excpected_result):
    assert calculate_sum(*input_list) == excpected_result


def test_calculate_sum_exception():
    with pytest.raises(ValueError, match="Empty list is passed"):
        calculate_sum()
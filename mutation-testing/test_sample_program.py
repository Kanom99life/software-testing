import sample_program
import pytest

def test_add_and_multiply():
    assert sample_program.add_and_multiply(3, 1) == 5

def test_compare_values():
    assert sample_program.compare_values(1) == 1
    assert sample_program.compare_values(2) == 3
    assert sample_program.compare_values(0) == 2

def test_boolean_operation():
    assert sample_program.boolean_operation(True) is True
    assert sample_program.boolean_operation(False) is False

def test_augment_assignment_example():
    assert sample_program.augment_assignment_example() == 15

def test_constant_usage():
    assert sample_program.constant_usage() == "Hello, World!"

def test_check_positive():
    assert sample_program.check_positive(5) is True
    with pytest.raises(ValueError):
        sample_program.check_positive(-1)
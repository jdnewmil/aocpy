"""AOC 2024 Day 2 test code."""

import pytest
from .. import day02

@pytest.fixture
def sample02() -> list[list[int]]:
    return [
        [7, 6, 4, 2, 1]
        , [1, 2, 7, 8, 9]
        , [9, 7, 6, 2, 1]
        , [1, 3, 2, 4, 5]
        , [8, 6, 4, 4, 1]
        , [1, 3, 6, 7, 9]]

def test_day02a(sample02):
    assert day02.is_safe(sample02[0])
    assert not day02.is_safe(sample02[1])
    assert not day02.is_safe(sample02[2])
    assert not day02.is_safe(sample02[3])
    assert not day02.is_safe(sample02[4])
    assert day02.is_safe(sample02[5])

def test_day01b(sample02):
    assert day02.is_anydrop_safe(sample02[0])
    assert not day02.is_anydrop_safe(sample02[1])
    assert not day02.is_anydrop_safe(sample02[2])
    assert day02.is_anydrop_safe(sample02[3])
    assert day02.is_anydrop_safe(sample02[4])
    assert day02.is_anydrop_safe(sample02[5])

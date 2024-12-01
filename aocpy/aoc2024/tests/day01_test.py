"""AOC 2024 Day 1 test code."""

import pytest
from .. import day01

@pytest.fixture
def sample01() -> tuple[list[int], list[int]]:
    return (
        [3, 4, 2, 1, 3, 3]
        , [4, 3, 5, 3, 9, 3])

def test_day01a(sample01):
    sorted_lists = day01.pairsort1(*sample01)
    dlist = day01.diff1(*sorted_lists)
    assert dlist == [2, 1, 0, 1, 2, 5]
    assert sum(dlist) == 11

def test_day01b(sample01):
    # sorted_lists = day01.pairsort1(*sample01)
    simlist = day01.similarity1(*sample01)
    assert simlist == [9, 4, 0, 0, 9, 9]

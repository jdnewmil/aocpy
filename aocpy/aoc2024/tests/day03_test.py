"""AOC 2024 Day 3 test code."""

import pytest
from .. import day01, day03

@pytest.fixture
def sample03() -> str:
    return (
        r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')

@pytest.fixture
def sample03b() -> str:
    return (
        r"mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")


def test_day03a(sample03):
    ans = day03.get_values_day03a(sample03)
    assert 161 == sum(ans)


def test_day03b(sample03b):
    ops = day03.get_ops_day03a(sample03b, ['mul', 'do', "don't"])
    cpu = day03.CPU2()
    ans = cpu.run(op_list=ops)
    assert ans == [8, 40]


"""AOC 2024 Day 11 test code."""

import pytest
from .. import day11


@pytest.fixture
def sample11_1() -> str:
    stones = '0 1 10 99 999'
    return stones


@pytest.fixture
def sample11_2() -> str:
    stones = '125 17'
    return stones


def test_day11a(sample11_1, sample11_2):
    stones1 = day11.parse_stones(sample11_1)
    assert day11.blink(stones1) == [
        1, 2024, 1, 0, 9, 9, 2021976]
    stones2 = day11.parse_stones(sample11_2)
    assert 55312 == len(day11.blinks(stones2, 25))


def test_day11b(sample11_1, sample11_2):
    stones1 = day11.parse_stones(sample11_1)
    assert day11.blink(stones1, fn1=day11.blink1b) == [
        1, 2024, 1, 0, 9, 9, 2021976]
    stones2 = day11.parse_stones(sample11_2)
    assert 55312 == len(day11.blinks(stones2, 25, day11.blink1b))
    stones2d = day11.to_stone_blinkd(stones2)
    stones2result = day11.blinkdsn(stones2d, 25)
    assert 55312 == day11.count_stone_blinkd(stones2result)

def test_agreement(sample11_2):
    stones2 = day11.parse_stones('0')
    stones2d = day11.to_stone_blinkd(stones2)
    for i in range(10):
        stones2 = day11.blink(stones2)
        stones2a = day11.to_stone_blinkd(stones2)
        stones2d = day11.blinkds(stones2d)
        assert stones2d == stones2a
    
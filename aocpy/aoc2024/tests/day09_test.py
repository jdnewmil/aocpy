"""AOC 2024 Day 9 test code."""

import pytest
from .. import day09

@pytest.fixture
def sample09() -> str:
    disk_map = "2333133121414131402"
    return disk_map


def test_day09a(sample09):
    ans1 = day09.expand_disk_map('12345')[0]
    assert ans1 == [0, -1, -1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, 2]
    ans2 = day09.compact_expanded_map(ans1)
    assert ans2 == [0, 2, 2, 1, 1, 1, 2, 2, 2, -1, -1, -1, -1, -1, -1]
    assert 1928 == day09.calc_day09a(sample09)

def test_day09b(sample09):
    assert 2858 == day09.calc_day09b(sample09)

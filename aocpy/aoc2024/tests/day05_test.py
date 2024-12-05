"""AOC 2024 Day 5 test code."""

import re
import pytest
from .. import day05

@pytest.fixture
def sample05() -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = [
        (47, 53), (97, 13), (97, 61), (97, 47), (75, 29), (61, 13), (75, 53)
        , (29, 13), (97, 29), (53, 29), (61, 53), (97, 53), (61, 29), (47, 13)
        , (75, 47), (97, 75), (47, 61), (75, 61), (47, 29), (75, 13), (53, 13)
    ]
    updates = [
        [75,47,61,53,29], [97,61,53,29,13], [75,29,13], [75,97,47,61,53]
        , [61,13,29], [97,13,75,29,47]
    ]
    return rules, updates


def test_day05a(sample05):
    rules, updates = sample05
    so = day05.build_sorted(rules)
    som = day05.build_so_map(so)
    assert day05.update_is_sorted(update=updates[0], som=som)
    assert day05.update_is_sorted(update=updates[1], som=som)
    assert day05.update_is_sorted(update=updates[2], som=som)
    assert not day05.update_is_sorted(update=updates[3], som=som)
    assert not day05.update_is_sorted(update=updates[4], som=som)
    assert not day05.update_is_sorted(update=updates[5], som=som)
    assert 143 == day05.calc_day05a(rules, updates)


def test_day05b(sample05):
    rules, updates = sample05
    assert 123 == day05.calc_day05b(rules, updates)

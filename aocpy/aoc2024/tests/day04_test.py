"""AOC 2024 Day 4 test code."""

import re
import pytest
from .. import day04

@pytest.fixture
def sample04() -> list[str]:
    return [
          'MMMSXXMASM'
        , 'MSAMXMSMSA'
        , 'AMXSXMAAMM'
        , 'MSAMASMSMX'
        , 'XMASAMXAMM'
        , 'XXAMMXXAMA'
        , 'SMSMSASXSS'
        , 'SAXAMASAAA'
        , 'MAMMMXMMMM'
        , 'MXMXAXMASX']

# @pytest.fixture
# def sample03b() -> str:
#     return (
#         r"mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")


def test_day04a(sample04):
    pat = re.compile('XMAS')
    rpat = re.compile('SAMX')
    test_s = 'MMXMAMXMASMXMAS'
    ans = day04.count_pat(pat, test_s)
    assert ans == 2
    assert day04.count_pat(rpat, test_s) == 0
    z = [s for s in day04.diag_iter(sample04, 4)]
    assert [z[i] for i in [0, 5, 6, 7, 12]] == [
        'SAMX', 'MMASMASMS', 'MSXMAXSAMX', 'MASAMXXAM', 'MMMX']
    ans = day04.count_day04a(sample04)
    assert 18 == ans


def test_day04b(sample04):
    assert  9 == day04.count_day04b(sample04)

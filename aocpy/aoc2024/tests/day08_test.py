"""AOC 2024 Day 8 test code."""

import pytest
from .. import day08

@pytest.fixture
def sample08() -> list[str]:
    trans_map = [
        "............"
        , "........0..."
        , ".....0......"
        , ".......0...."
        , "....0......."
        , "......A....."
        , "............"
        , "............"
        , "........A..."
        , ".........A.."
        , "............"
        , "............"]
    return trans_map


def test_day08a(sample08):
    ans = day08.parse_trans_map(sample08)
    assert (8, 1) in ans['0']
    x = day08.IntPoint(value=(4, 3))
    y = day08.IntPoint(value=(5, 5))
    assert (9, 8) == (x + y).value
    assert (8, 6) == (x * 2).value
    bounds = (len(sample08[0]), len(sample08))
    ans2 = day08.find_antinode_pair(x.value, y.value, bounds=bounds)
    assert 2 == len(ans2)
    assert (3, 1) in ans2
    assert (6, 7) in ans2
    ans3 = day08.find_xmit_antinodes(ans, bounds=bounds)
    assert 14 == len(ans3['0'] | ans3['A'])


def test_day08b(sample08):
    ans = day08.parse_trans_map(sample08)
    bounds = (len(sample08[0]), len(sample08))
    assert 34 == day08.calc_day08b(ans, bounds=bounds)
    

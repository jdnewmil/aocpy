"""AOC 2024 Day 6 test code."""

import re
import pytest
from .. import day06

@pytest.fixture
def sample06() -> list[str]:
    grid_room = [
        '....#.....'
        , '.........#'
        , '..........'
        , '..#.......'
        , '.......#..'
        , '..........'
        , '.#..^.....'
        , '........#.'
        , '#.........'
        , '......#...'
    ]
    return grid_room


def test_day06a(sample06):
    guard_initial_loc = day06.find_guard(sample06)
    assert (4, 6, day06.UP) == guard_initial_loc
    trail = day06.map_guard_trail(sample06, guard_initial_loc) # type: ignore
    assert 41 == len(day06.get_positions(trail_set=trail))

def test_day06b(sample06):
    guard_initial_loc = day06.find_guard(sample06)
    assert 6 == len(day06.find_loop_positions(sample06, guard_initial_loc))

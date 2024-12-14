"""AOC 2024 Day 14 test code."""

import pytest
from .. import day14


@pytest.fixture
def sample14() -> list[str]:
    lns = [
        'p=0,4 v=3,-3'
        , 'p=6,3 v=-1,-3'
        , 'p=10,3 v=-1,2'
        , 'p=2,0 v=2,-1'
        , 'p=0,0 v=1,3'
        , 'p=3,0 v=-2,-2'
        , 'p=7,6 v=-1,-3'
        , 'p=3,0 v=-1,-2'
        , 'p=9,3 v=2,3'
        , 'p=7,3 v=-1,2'
        , 'p=2,4 v=2,-3'
        , 'p=9,5 v=-3,-3']
    return lns


def test_day14a(sample14):
    rlist = day14.parse_robots_data(sample14)
    assert 12 == len(rlist)
    field_dim = day14.IntVec(value=(11, 7))
    assert 12 == day14.calc_day14a(sample14, field_dim=field_dim)


def test_day14b(sample14):
    assert False

    
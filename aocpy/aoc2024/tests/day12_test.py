"""AOC 2024 Day 12 test code."""

import pytest
from .. import day12


@pytest.fixture
def sample12_1() -> list[str]:
    raw_map = [
        'AAAA'
        , 'BBCD'
        , 'BBCC'
        , 'EEEC'
    ]
    return raw_map


@pytest.fixture
def sample12_2() -> list[str]:
    raw_map = [
        'OOOOO'
        , 'OXOXO'
        , 'OOOOO'
        , 'OXOXO'
        , 'OOOOO'
    ]
    return raw_map


def test_day12a(sample12_1, sample12_2):
    m1 = day12.build_merge_map(sample12_1)
    dims = (len(sample12_1[0]), len(sample12_1))
    assert day12.loc(m1, 0, 0, dims) == (True, False, True, True)
    assert day12.loc(m1, 0, 1, dims) == (True, False, False, True)
    rlen, rm = day12.mark_regions(m1, dims)
    assert rlen == 5
    assert rm == [[0, 0, 0, 0], [1, 1, 2, 3], [1, 1, 2, 2], [4, 4, 4, 2]]
    areas = day12.calc_areas(rm, rlen)
    assert areas == [4, 4, 4, 1, 3]
    perims = day12.calc_perimeters(rm, m1, rlen, areas)
    assert perims == [10, 8, 10, 4, 8]

    m2 = day12.build_merge_map(sample12_2)
    dims = (len(sample12_2[0]), len(sample12_2))
    rlen, rm = day12.mark_regions(m2, dims)
    areas = day12.calc_areas(rm, rlen)
    perims = day12.calc_perimeters(rm, m2, rlen, areas)
    assert 772 == day12.calc_price(areas, perims)



def test_day12b(sample12_1, sample12_2):
    assert False

    
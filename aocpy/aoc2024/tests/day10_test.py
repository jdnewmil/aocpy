"""AOC 2024 Day 10 test code."""

import pytest
from .. import day10

@pytest.fixture
def sample10() -> list[str]:
    topo_map = [
        '89010123'
        , '78121874'
        , '87430965'
        , '96549874'
        , '45678903'
        , '32019012'
        , '01329801'
        , '10456732'   
    ]
    return topo_map


def test_day10a(sample10):
    elev_map = day10.parse_topo_map(sample10)
    elev0_set = day10.find_elevs(elev_map=elev_map, target_elev=0)
    headings = day10.find_headings(elev_map=elev_map)
    t_heads = day10.find_trailheads(elev_map=elev_map, headings=headings, elev0_set=elev0_set)
    assert 36 == sum([len(s) for th, s in t_heads.items()])

def test_day10b(sample10):
    elev_map = day10.parse_topo_map(sample10)
    elev0_set = day10.find_elevs(elev_map=elev_map, target_elev=0)
    headings = day10.find_headings(elev_map=elev_map)
    trails0 = day10.find_trails_trailhead(elev_map=elev_map, headings=headings, start=(2, 0))
    assert 20 == len(trails0)
    assert 81 == day10.calc_day10b(topo_map=sample10)

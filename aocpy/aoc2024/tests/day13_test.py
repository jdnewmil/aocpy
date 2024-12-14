"""AOC 2024 Day 13 test code."""

import pytest
from .. import day13


@pytest.fixture
def sample13() -> list[str]:
    lns = [
        'Button A: X+94, Y+34'
        , 'Button B: X+22, Y+67'
        , 'Prize: X=8400, Y=5400'
        , ''
        , 'Button A: X+26, Y+66'
        , 'Button B: X+67, Y+21'
        , 'Prize: X=12748, Y=12176'
        , ''
        , 'Button A: X+17, Y+86'
        , 'Button B: X+84, Y+37'
        , 'Prize: X=7870, Y=6450'
        , ''
        , 'Button A: X+69, Y+23'
        , 'Button B: X+27, Y+71'
        , 'Prize: X=18641, Y=10279']
    return lns


@pytest.fixture
def sample13_2() -> list[str]:
    lns = [
        'Button A: X+10, Y+20'
        , 'Button B: X+20, Y+40'
        , 'Prize: X=100, Y=200']
    return lns


def test_day13a(sample13, sample13_2):
    cm = day13.parse_claw_machine(sample13[0:3])
    assert cm.buttons['A'] == (94, 34)
    assert cm.buttons['B'] == (22, 67)
    assert cm.prize == (8400, 5400)
    lns_list = day13.split_list_at_value(sample13)
    assert 4 == len(lns_list)
    cms = day13.parse_claw_machines(lns_list=lns_list)
    assert 4 == len(cms)
    solns = day13.solve_claw_machines(cms)
    assert solns == [(80, 40), (0, 0), (38, 86), (0, 0)]
    lns_list2 = day13.split_list_at_value(sample13_2)
    cms2 = day13.parse_claw_machines(lns_list2)
    solns2 = day13.solve_claw_machines(cms2)
    assert solns2 == [(0, 5)]
    assert 480 == day13.calc_day13a(sample13)


def test_day13b(sample13):
    assert 875318608908 == day13.calc_day13b(sample13)

    
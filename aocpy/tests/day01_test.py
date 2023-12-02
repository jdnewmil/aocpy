# test_day01.py

import pathlib
import pytest
from aocpy.aoc2022 import day01

def test_split_list():
    l1 = ['a', 'a', '', 'b']
    a1 = [l for l in day01.split_list(l1)]
    assert a1 == [['a', 'a'], ['b']]
    l2 = ['', 'a', 'a', '', 'b']
    a2 = [l for l in day01.split_list(l2)]
    assert a2 == [['a', 'a'], ['b']]
    l3 = ['a', 'a', '', '', 'b']
    a3 = [l for l in day01.split_list(l3)]
    assert a3 == [['a', 'a'], ['b']]
    l4 = ['a', 'a', '', 'b', '']
    a4 = [l for l in day01.split_list(l4)]
    assert a4 == [['a', 'a'], ['b']]


@pytest.fixture
def dta_dir():
    return pathlib.Path(__file__).parent / 'data'


@pytest.fixture
def sample_day01(dta_dir):
    return day01.read_elf_loads(dta_dir / 'day01a.txt')


def test_find_max_load(sample_day01):
    ans_i, ans_load = day01.find_max_load(sample_day01)
    assert ans_i == 3
    assert ans_load == 24000.


def test_find_max_load3(sample_day01):
    ans = day01.find_max_load3(sample_day01)
    assert ans == [(24000.0, 3), (11000.0, 2), (10000.0, 4)]

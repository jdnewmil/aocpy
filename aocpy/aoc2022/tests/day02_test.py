# day02_test.py

import pathlib
import pytest
from .. import day02

@pytest.fixture
def dta_dir():
    return pathlib.Path(__file__).parent / 'data'


@pytest.fixture
def sample_day02(dta_dir):
    return day02.read_rps_strategy(dta_dir / 'day02a.txt')


def test_gen_rps_results(sample_day02):
    ans = list(day02.gen_rps_results(sample_day02))
    assert ans == [8, 1, 6]


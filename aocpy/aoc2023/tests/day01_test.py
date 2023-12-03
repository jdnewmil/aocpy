# day01_test.py

import pytest
from .. import day01


@pytest.fixture
def testdta_01a() -> list[str]:
    return [
        '1abc2'
        , 'pqr3stu8vwx'
        , 'a1b2c3d4e5f'
        , 'treb7uchet']

@pytest.fixture
def testdta_01b() -> list[str]:
    return [
        'two1nine'
        , 'eightwothree'
        , 'abcone2threexyz'
        , 'xtwone3four'
        , '4nineeightseven2'
        , 'zoneight234'
        , '7pqrstsixteen']

def test_find_first_digit(testdta_01a):
    ans = day01.find_first_digit_pos(testdta_01a[0])
    assert ans == 0

def test_find_last_digit(testdta_01a):
    ans = day01.find_last_digit_pos(testdta_01a[0])
    assert ans == 4

def test_find_firstandlast_digits(testdta_01a):
    ans = day01.find_firstandlast_digits(testdta_01a[0])
    assert ans == '12'

def test_calc_calibration_sum(testdta_01a):
    ans = day01.calc_calibration_sum(testdta_01a)
    assert ans == 142


def test_calc_pat_calibration_sum(testdta_01b):
    ans = day01.calc_pat_calibration_sum(testdta_01b)
    assert ans == 281


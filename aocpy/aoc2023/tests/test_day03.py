# test_day03.py

#import pathlib
import pytest
from .. import day03


@pytest.fixture
def testdta_03a():
    return [
        '467..114..'
        , '...*......'
        , '..35..633.'
        , '......#...'
        , '617*......'
        , '.....+.58.'
        , '..592.....'
        , '......755.'
        , '...$.*....'
        , '.664.598..']


@pytest.fixture
def testdta_03a2():
    return [
        '123....456'
        , '...*......'
        , '.35.633...'
        , '..........'
        , '...13.19..'
        , '.....&....'
        , '..........'
        , '617*15....'
        , '..........'
        , '$85....58*'
        , '....*.....'
        , '.. 592....'
        , '.....75...'
        , '4....*....'
        , '664....598'
        , '..........'
        , '248^..^842']


@pytest.fixture
def testnumpos_03a(testdta_03a) -> set[tuple]:
    return day03.find_numbers_03a(testdta_03a)


@pytest.fixture
def testnumpos_03a2(testdta_03a2) -> set[tuple]:
    return day03.find_numbers_03a(testdta_03a2)


def test_find_partnumbers_03a(testdta_03a):
    ans = day03.find_numbers_03a(testdta_03a)
    assert 10 == len(ans)


def test_find_partnumbers_03a2(testdta_03a2):
    ans = day03.find_numbers_03a(testdta_03a2)
    assert 17 == len(ans)


def test_extract_part_numbers(testdta_03a, testnumpos_03a):
    ans = day03.extract_part_numbers(testdta_03a, testnumpos_03a)
    assert not 114 in ans
    assert 664 in ans


def test_extract_part_numbers2(testdta_03a2, testnumpos_03a2):
    ans = day03.extract_part_numbers(testdta_03a2, testnumpos_03a2)
    assert not 664 in ans  # digits only
    assert not 4 in ans    # digits only
    assert 633 in ans  # UL
    assert 35 in ans   # UR
    assert 19 in ans   # LL
    assert 13 in ans   # LR
    assert 15 in ans   # L
    assert 617 in ans  # R
    assert 592 in ans  # U
    assert 75 in ans   # D
    assert 248 in ans  # Left edge
    assert 842 in ans  # Right edge


def test_get_numberpos_left(testdta_03a):
    ans = day03.get_numberpos_left(testdta_03a[0], (0, 1))
    assert (0, 0, 2) == ans  # ignores digits to right
    ans1 = day03.get_numberpos_left(testdta_03a[2], (2, 7))
    assert (2, 6, 8) == ans1  # ignores digits to right


def test_get_numberpos_right(testdta_03a):
    ans = day03.get_numberpos_right(testdta_03a[0], (0, 1))
    assert (0, 1, 3) == ans  # ignores digits to left
    ans1 = day03.get_numberpos_right(testdta_03a[2], (2, 7))
    assert (2, 7, 9) == ans1  # ignores digits to left


def test_get_numberpos_mid(testdta_03a):
    ans = day03.get_numberpos_mid(testdta_03a[0], (0, 1))
    assert (0, 0, 3) == ans
    ans1 = day03.get_numberpos_mid(testdta_03a[2], (2, 7))
    assert (2, 6, 9) == ans1


def test_extract_coordadjacent_numberposs(testdta_03a):
    ans = day03.extract_coordadjacent_numberposs(testdta_03a, (8, 5))
    assert 2 == len(ans)


def test_extract_gears_numposs(testdta_03a):
    ans = day03.extract_gears_numposs(testdta_03a)
    assert 2 == len(ans)


def test_calc_gear_ratios(testdta_03a):
    ans = day03.calc_gear_ratios(testdta_03a)
    assert {(1,3): 16345, (8, 5): 451490} == ans


def test_calc_gear_ratios_sum(testdta_03a):
    gr_dict = day03.calc_gear_ratios(testdta_03a)
    ans = day03.calc_gear_ratios_sum(gr_dict)
    assert 467835 == ans


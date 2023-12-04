# test_day04.py

#import pathlib
import pytest
from .. import day04


@pytest.fixture
def testdta_04a():
    return [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        , 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'
        , 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
        , 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'
        , 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
        , 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']


@pytest.fixture
def testcards_04a(testdta_04a):
    return day04.parse_cards(testdta_04a)


def test_parse_lines(testdta_04a):
    ans = day04.parse_cards(testdta_04a)
    assert 6 == len(ans)


def test_count_card_matches(testcards_04a):
    ans = day04.count_card_matches(testcards_04a[0])
    assert ans == 4


def test_calc_points(testcards_04a):
    ans = day04.calc_points(testcards_04a)
    assert ans == 13


def test_count_copies(testcards_04a):
    matches = day04.count_matches(testcards_04a)
    match_copies = day04.count_copies(matches)
    assert 30 == sum(match_copies)

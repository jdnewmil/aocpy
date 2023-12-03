# day02_test.py

import pytest
from .. import day02


@pytest.fixture
def testdta_02a() -> list[str]:
    return [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        , 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
        , 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
        , 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
        , 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

@pytest.fixture
def testcols_02a() -> dict:
    return {
        'red': 12
        , 'green': 13
        , 'blue': 14}


@pytest.fixture
def testgames_02a(testdta_02a) -> list:
    return day02.parse_games(testdta_02a)


def test_parse_col():
    ans = day02.parse_col(' 3 blue')
    assert ans == (3, 'blue')

def test_parse_round():
    ans = day02.parse_round(' 3 blue, 4 red')
    assert ans['blue'] == 3
    assert ans['red'] == 4

def test_parse_rounds(testdta_02a):
    ans = day02.parse_rounds(testdta_02a[0][7:])
    assert ans[0]['blue'] == 3
    assert ans[0]['red'] == 4
    assert ans[1]['green'] == 2

def test_parse_game(testdta_02a):
    ans = day02.parse_game(testdta_02a[0])
    assert ans['rounds'][0]['blue'] == 3
    assert ans['game'] == 1

def test_parse_games(testdta_02a):
    ans = day02.parse_games(testdta_02a)
    assert len(ans) == 5

def test_find_color_max(testdta_02a):
    rounds = day02.parse_rounds(testdta_02a[0][7:])
    ans = day02.find_color_max(rounds, 'blue')
    assert ans == 6
    ans2 = day02.find_color_max(rounds, 'bluex')
    assert ans2 == 0


def test_check_game_02a(testdta_02a, testcols_02a):
    game = day02.parse_game(testdta_02a[0])
    ans = day02.check_game_02a(game, testcols_02a)
    assert ans


def test_calc_possible_02a(testdta_02a, testcols_02a):
    games = day02.parse_games(testdta_02a)
    ans = day02.calc_possible_02a(games, testcols_02a)
    assert ans == 8


def test_calc_game_power(testgames_02a):
    ans = day02.calc_game_power(testgames_02a[0])
    assert 48 == ans


def test_calc_games_power(testgames_02a):
    ans = day02.calc_games_power(testgames_02a)
    assert 2286 == ans


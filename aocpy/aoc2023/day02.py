# day02.py
"""Computation for 2023 day 2"""

#import re

def readlines(fname: str) -> list[str]:
    with open(fname, encoding='UTF-8') as f:
        lines = f.readlines()
    return [
        s.strip()
        for s in lines]


def parse_col(s: str) -> tuple:
    ss = s.strip()
    v = ss.split(' ')
    return (int(v[0]), v[1])


def parse_round(s: str) -> dict:
    cols = s.split(',')
    return {
        c[1]: c[0]
        for c in (parse_col(cs) for cs in cols)}


def parse_rounds(s: str) -> list:
    rnds = s.split(';')
    return [
        parse_round(rs)
        for rs in rnds]


def parse_game(s: str) -> dict:
    v0 = s.split(':')
    return {
        'game': int(v0[0][5:])
        , 'rounds': parse_rounds(v0[1])}


def parse_games(v: list[str]) -> list:
    return [
        parse_game(line)
        for line in v]


def find_color_max(rounds: list, col: str) -> int:
    result = 0
    for round in rounds:
        if col in round:
            result = max(round[col], result)
    return result


def check_game_02a(game: dict, check_cols: dict) -> bool:
    for col, n in check_cols.items():
        if n < find_color_max(game['rounds'], col):
            return False
    return True


def filter_possible_games_02a(games: list, check_cols: dict) -> list:
    return [
        game
        for game in games
        if check_game_02a(game, check_cols)]


def calc_possible_02a(games: list, check_cols: dict) -> int:
    result = 0
    for game in games:
        if check_game_02a(game, check_cols):
            result += game['game']
    return result


def get_game_colors(game: dict) -> set:
    result = set()
    for round in game['rounds']:
        result = result.union(set(round.keys()))
    return result


def calc_game_power(game: dict) -> int:
    result = 1
    for col in get_game_colors(game):
        result *= find_color_max(game['rounds'], col)
    return result


def calc_games_power(games: list) -> int:
    return sum([
        calc_game_power(game)
        for game in games])


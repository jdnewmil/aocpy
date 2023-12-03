# day01.py
"""Computation for 2023 day 1"""

import re

def find_first_digit_pos(s: str) -> int:
    pos = 0
    while pos < len(s) and not s[pos].isdigit():
        pos += 1
    return pos


def find_last_digit_pos(s: str) -> int:
    pos = len(s) - 1
    while 0 < pos and not s[pos].isdigit():
        pos -= 1
    return pos


def find_firstandlast_digits(s: str) -> str:
    return (
        s[find_first_digit_pos(s)]
        + s[find_last_digit_pos(s)])

def calc_calibration_sum(v: list[str]) -> int:
    accum = 0
    for s in v:
        accum += int(find_firstandlast_digits(s))
    return accum

digits_dict = {
    #'0': 0
    #, 'zero': 0
    '1': 1
    , 'one': 1
    , '2': 2
    , 'two': 2
    , '3': 3
    , 'three': 3
    , '4': 4
    , 'four': 4
    , '5': 5
    , 'five': 5
    , '6': 6
    , 'six': 6
    , '7': 7
    , 'seven': 7
    , '8': 8
    , 'eight': 8
    , '9': 9
    , 'nine': 9}

def find_firstandlast_re(
    s: str
    , reg: re.Pattern
    , subpats: dict[str, int]
) -> list[int]:
    matches = reg.findall(s)
    return [
        subpats[matches[0]], subpats[matches[-1]]]
    

def find_firstandlast_pats(v: list[str], subpats: dict[str, int]) -> list[int]:
    patlist = [k for k in subpats.keys()]
    # (?= lookahead allows finding overlapped matches
    pat_core_pat = '(?=(' + '|'.join(patlist) + '))'
    pat_core_re = re.compile(pat_core_pat)
    return [
        find_firstandlast_re(s, pat_core_re, subpats)
        for s in v]

def calc_pat_calibration_sum(v: list[str]) -> int:
    vals = find_firstandlast_pats(v, digits_dict)
    return sum(
        [
            i[0] * 10 + i[1]
            for i in vals])

"""AOC 2024 Day04 functions."""

from typing import Optional, TypeAlias
from dataclasses import dataclass
import re


def count_pat(pat: re.Pattern, s: str) -> int:
    return len(pat.findall(s))


def transpose(matrix: list[str]) -> list[str]:
    return [''.join(t) for t in zip(*matrix)]


class diag_iter:
    def __init__(self, matrix: list[str], min_len: int) -> None:
        self.min_len = min_len
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
    
    def __iter__(self):
        m = self.matrix
        jnum = self.rows - self.min_len
        for j0 in range(jnum, 0, -1):
            yield ''.join(
                [
                    m[j][i]
                    for i, j in zip(range(self.cols), range(j0, self.rows))
                ]
            )
        inum = self.cols - self.min_len
        for i0 in range(inum + 1):
            yield ''.join(
                [
                    m[j][i]
                    for i, j in zip(range(i0, self.cols), range(self.rows))
                ]
            )


def count_day04a(matrix: list[str]) -> int:
    pat = re.compile('XMAS')
    rpat = re.compile('SAMX')
    result = 0
    # count in rows
    for s in matrix:
        result += count_pat(pat, s)
        result += count_pat(rpat, s)
    # count in diagonals
    for s in diag_iter(matrix, 4):
        result += count_pat(pat, s)
        result += count_pat(rpat, s)
    # count in columns
    m = transpose(matrix)
    for s in m:
        result += count_pat(pat, s)
        result += count_pat(rpat, s)
    # count in other diagonals
    m = matrix.copy()
    m.reverse()
    for s in diag_iter(m, 4):
        result += count_pat(pat, s)
        result += count_pat(rpat, s)
    return result

def get_corners(matrix: list[str], i: int, j: int) -> str:
    x = (-1, 1)
    return ''.join(
        matrix[j + a][i + b]
        for a in x
        for b in x)


def check_corners(matrix: list[str], i: int, j: int) -> int:
    s = get_corners(matrix, i, j)
    if s in ('MMSS', 'SMSM', 'SSMM', 'MSMS'):
        return 1
    return 0


def count_day04b(matrix: list[str]) -> int:
    result = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(1, cols - 1):
        for j in range(1, rows - 1):
            if 'A' == matrix[j][i]:
                result += check_corners(matrix, i, j)
    return result

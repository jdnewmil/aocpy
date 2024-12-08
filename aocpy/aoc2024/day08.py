"""AOC 2024 Day08 functions."""

from typing import Optional, TypeAlias, Callable, Self
from dataclasses import dataclass
from itertools import permutations

RawPoint: TypeAlias = tuple[int, int]
TransDict: TypeAlias = dict[str,set[RawPoint]]
AntinodeSearch: TypeAlias = \
    Callable[[RawPoint, RawPoint, RawPoint], set[RawPoint]]


def parse_trans_map(trans_map: list[str]) -> TransDict:
    i_count = len(trans_map[0])
    j_count = len(trans_map)
    result = dict()
    for j in range(j_count):
        for i in range(i_count):
            c = trans_map[j][i]
            if '.' != c:
                if c in result:
                    result[c] |= set([(i, j)])
                else:
                    result[c] = set([(i, j)])
    return result


@dataclass
class IntPoint:
    value: RawPoint

    def __add__(self, y) -> Self:
        return mkIntPoint(
            value=(
                self.value[0] + y.value[0]
                , self.value[1] + y.value[1])) # type: ignore

    def __sub__(self, y) -> Self:
        return mkIntPoint(
            value=(
                self.value[0] - y.value[0]
                , self.value[1] - y.value[1])) # type: ignore

    def __mul__(self, y: int) -> Self:
        return mkIntPoint(
            value=(
                self.value[0] * y
                , self.value[1] * y)) # type: ignore


def mkIntPoint(value: RawPoint) -> IntPoint:
    return IntPoint(value)


def is_raw_point_in_bounds(raw_point: RawPoint, bounds: RawPoint) -> bool:
    if raw_point[0] < 0 or raw_point[1] < 0:
        return False
    return raw_point[0] < bounds[0] and raw_point[1] < bounds[1]


def find_antinode_pair(
    xmit0: RawPoint
    , xmit1: RawPoint
    , bounds: RawPoint
) -> set[RawPoint]:
    a = IntPoint(value=xmit0)
    b = IntPoint(value=xmit1)
    d = a - b
    result = set()
    an0 = (b + d * 2).value
    if is_raw_point_in_bounds(an0, bounds=bounds):
        result |= set([an0])
    an1 = (b - d).value
    if is_raw_point_in_bounds(an1, bounds=bounds):
        result |= set([an1])
    return result


def find_antinode_set(
    xmit0: RawPoint
    , xmit1: RawPoint
    , bounds: RawPoint
) -> set[RawPoint]:
    a = IntPoint(value=xmit0)
    b = IntPoint(value=xmit1)
    d = a - b
    result = set([a.value, b.value])
    an_test = a + d
    while is_raw_point_in_bounds(an_test.value, bounds=bounds):
        result.add(an_test.value)
        an_test += d
    an_test = b - d
    while is_raw_point_in_bounds(an_test.value, bounds=bounds):
        result.add(an_test.value)
        an_test -= d
    return result
    


def find_antinodes(
    xmit_set: set[RawPoint]
    , bounds: RawPoint
    , an_func: AntinodeSearch = find_antinode_pair
) -> set[RawPoint]:
    result = set()
    for xmit0, xmit1 in permutations(xmit_set, 2):
        result |= an_func(xmit0, xmit1, bounds)
    return result


def find_xmit_antinodes(
    xnodes: TransDict
    , bounds: RawPoint
    , an_func: AntinodeSearch = find_antinode_pair
) -> TransDict:
    return {
        xtype: find_antinodes(s, bounds=bounds, an_func=an_func)
        for xtype, s in xnodes.items()}


def calc_day08a(xnodes: TransDict, bounds: RawPoint) -> int:
    xa = find_xmit_antinodes(xnodes=xnodes, bounds=bounds)
    result = set()
    for xtype, s in xa.items():
        result |= s
    return len(result)

def calc_day08b(xnodes: TransDict, bounds: RawPoint) -> int:
    xa = find_xmit_antinodes(
        xnodes=xnodes
        , bounds=bounds
        , an_func=find_antinode_set)
    result = set()
    for xtype, s in xa.items():
        result |= s
    return len(result)

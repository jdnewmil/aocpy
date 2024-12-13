"""AOC 2024 Day12 functions."""

from typing import TypeAlias, TypeVar, Optional, Sequence

RawMap: TypeAlias = list[Sequence]
MergeCell: TypeAlias = tuple[bool, bool, bool, bool]
MergeMap: TypeAlias = list[list[MergeCell]]
RegionMap: TypeAlias = list[list[int]]
PlotLocs: TypeAlias = list[tuple[int, int]]
RegionPlots: TypeAlias = list[PlotLocs]
RegionValues: TypeAlias = list[int]

UP: int = 0
RIGHT: int = 1
DOWN: int = 2
LEFT: int = 3

T = TypeVar('T')


def loc(map_: list[Sequence[T]], i: int, j: int, dims: tuple[int, int]) -> Optional[T]:
    if i < 0 or dims[0] <= i or j < 0 or dims[1] <= j:
        return None
    return map_[j][i]


def build_merge_map(raw_map: RawMap) -> MergeMap:
    dims = (len(raw_map[0]), len(raw_map))
    return [
        [
            (
                c != loc(raw_map, i, j - 1, dims)
                , c != loc(raw_map, i + 1, j, dims)
                , c != loc(raw_map, i, j + 1, dims)
                , c != loc(raw_map, i - 1, j, dims))
            for i, c in enumerate(row)]
        for j, row in enumerate(raw_map)]


def create_region_map(dims: tuple[int, int]) -> RegionMap:
    return [
        [
            -1
            for i in range(dims[0])]
        for j in range(dims[1])]


def mark_region(
    rm: RegionMap  # mutates
    , mm: MergeMap  # no mutation
    , start: tuple[int, int]
    , region_num: int
):
    todo = [start]  # stack
    while 0 < len(todo):
        cur = todo.pop()
        i, j = cur
        rm[j][i] = region_num
        borders = mm[j][i]
        j1 = j - 1
        if not borders[UP] and rm[j1][i] < 0:
            todo.append((i, j1))
        j1 = j + 1
        if not borders[DOWN] and rm[j1][i] < 0:
            todo.append((i, j1))
        i1 = i - 1
        if not borders[LEFT] and rm[j][i1] < 0:
            todo.append((i1, j))
            rm[j][i1] = region_num
        i1 = i + 1
        if not borders[RIGHT] and rm[j][i1] < 0:
            todo.append((i1, j))


def mark_regions(mm: MergeMap, dims: tuple[int, int]) -> tuple[int, RegionMap]:
    i_dim, j_dim = dims
    rm = create_region_map(dims)
    cur_region = -1
    for j in range(j_dim):
        for i in range(i_dim):
            if rm[j][i] < 0:
                cur_region += 1
                mark_region(rm, mm, (i, j), cur_region)
    return cur_region + 1, rm


def calc_areas(rm: RegionMap, r_len: int) -> RegionValues:
    result = [0] * r_len
    for row in rm:
        for r in row:
            result[r] += 1
    return result

def calc_perimeters(rm: RegionMap, mm: MergeMap, r_len: int, r_areas: RegionValues) -> RegionValues:
    borders = [0] * r_len
    for j, row in enumerate(mm):
        for i, mc in enumerate(row):
            r = rm[j][i]
            borders[r] += sum(mc)
    return borders

def calc_price(areas: RegionValues, perims: RegionValues) -> int:
    return sum(
        [
            a * p
            for a, p in zip(areas, perims)])

def calc_day12a(lns: list[str]) -> int:
    mm = build_merge_map(lns)
    dims = (len(lns[0]), len(lns))
    rlen, rm = mark_regions(mm, dims)
    areas = calc_areas(rm, rlen)
    perims = calc_perimeters(rm, mm, rlen, areas)
    return calc_price(areas, perims)


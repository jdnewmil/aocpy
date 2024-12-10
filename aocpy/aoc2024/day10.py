"""AOC 2024 Day10 functions."""

from typing import TypeAlias, Self
from dataclasses import dataclass


RawLoc: TypeAlias = tuple[int, int]
RawPath: TypeAlias = tuple[tuple, RawLoc]

@dataclass
class IntVec:
    value: RawLoc

    def __add__(self, y) -> Self:
        return IntVec(
            value=(
                self.value[0] + y.value[0]
                , self.value[1] + y.value[1])) # type: ignore

    def __sub__(self, y) -> Self:
        return IntVec(
            value=(
                self.value[0] - y.value[0]
                , self.value[1] - y.value[1])) # type: ignore

    def __mul__(self, y: int) -> Self:
        return IntVec(
            value=(
                self.value[0] * y
                , self.value[1] * y)) # type: ignore


UP: int = 0
RIGHT: int = 1
DOWN: int = 2
LEFT: int = 3

dir_set: set[int] = set([UP, RIGHT, DOWN, LEFT])
vdirs: list[IntVec] = [
    IntVec((0, -1)), IntVec((1, 0)), IntVec((0, 1)), IntVec((-1, 0))]
c_elev_set: set[str] = set([str(i) for i in range(10)])

LocHeading: TypeAlias = tuple[IntVec, int]
LocHeadingStack: TypeAlias = list[LocHeading]

OUTSIDE: RawLoc = (-1, -1)

def flip_dir(dir: int) -> int:
    return [2, 3, 0, 1][dir]


def do_step(pos: IntVec, dir: int, bounds: RawLoc) -> IntVec:
    result = pos + vdirs[dir]
    if dir % 2:  # right or left
        rl = result.value[0]
        if rl < 0 or bounds[0] < rl:
            return IntVec(OUTSIDE)
    else:
        ud = result.value[1]
        if ud < 0 or bounds[1] < ud:
            return IntVec(OUTSIDE)
    return result


def find_elevs(elev_map: list[str], target_elev: int) -> set[RawLoc]:
    result = set()
    for j, row in enumerate(elev_map):
        for i, e in enumerate(row):
            if e == target_elev:
                result.add((i, j))
    return result


def parse_topo_map(topo_map: list[str]) -> list[list[int]]:
    return [
        [
            int(c)
            for i, c in enumerate(row)]
        for j, row in enumerate(topo_map)]


def find_headings(elev_map: list[list[int]], step_size: int = 1) -> dict[RawLoc, set[RawLoc]]:
    bounds = (len(elev_map[0]) - 1, len(elev_map) - 1)
    result = {}
    for j, row in enumerate(elev_map):
        for i, elev in enumerate(row):
            raw_loc = (i, j)
            loc = IntVec(raw_loc)
            expected_elev = elev + step_size
            for heading in dir_set:
                next_loc = do_step(loc, heading, bounds)
                next_i, next_j = next_loc.value
                if OUTSIDE != next_loc.value:
                    next_elev = elev_map[next_j][next_i]
                    if next_elev == expected_elev:
                        if raw_loc in result:
                            result[raw_loc].add(next_loc.value)
                        else:
                            result[raw_loc] = set([next_loc.value])
                if raw_loc not in result:
                    result[raw_loc] = set()
    return result


def find_trailpeaks(
    elev_map: list[list[int]]
    , headings: dict[RawLoc, set[RawLoc]]
    , start: RawLoc
    , peak_elev: int = 9
) -> set[RawLoc]:
    todo = [start]
    visited = set()
    result = set()
    while 0 < len(todo):
        cur = todo.pop()
        i, j = cur
        if peak_elev == elev_map[j][i]:
            result.add(cur)
        elif cur in headings:
            todo.extend(
                [
                    nxt
                    for nxt in headings[cur]
                    if not cur in visited])
        visited.add(cur)
    return result


def find_trails_trailhead(
    elev_map: list[list[int]]
    , headings: dict[RawLoc, set[RawLoc]]
    , start: RawLoc
    , peak_elev: int = 9
) -> set[RawPath]:
    todo = [(tuple(), start)]
    visited = set()
    result = set()
    while 0 < len(todo):
        cur_path = todo.pop()
        prev_path, cur = cur_path
        i, j = cur
        if peak_elev == elev_map[j][i]:
            result.add(cur_path)
        elif cur_path not in visited:
            todo.extend(
                [
                    (cur_path, nxt)
                    for nxt in headings[cur]])
        visited.add(cur_path)
    return result


def find_trailheads(
    elev_map: list[list[int]]
    , headings: dict[RawLoc, set[RawLoc]]
    , elev0_set: set[RawLoc]
) -> dict[RawLoc, set[RawLoc]]:
    """Find trailheads.

    Parameters
    ----------
    headings : dict[RawLoc, set[RawLoc]]
        Given map of headings.
    elev0_set : set[RawLoc]
        Set of possible trailheads
        
    Returns
    -------
    dict[RawLoc, set[Rawloc]]
        Keys are trailheads, values are sets of peaks
        associated with those trailheads.
    """
    result = {}

    for e0 in elev0_set:
        result[e0] = find_trailpeaks(
            elev_map=elev_map
            , headings=headings
            , start=e0)
    return result


def find_all_trails_trailhead(
    elev_map: list[list[int]]
    , headings: dict[RawLoc, set[RawLoc]]
    , elev0_set: set[RawLoc]
) -> dict[RawLoc, set[RawPath]]:
    return {
        e0: find_trails_trailhead(
            elev_map=elev_map
            , headings=headings
            , start=e0)
        for e0 in elev0_set}


def calc_day10a(topo_map: list[str]) -> int:
    elev_map = parse_topo_map(topo_map)
    elev0_set = find_elevs(elev_map=elev_map, target_elev=0)
    headings = find_headings(elev_map=elev_map)
    t_heads = find_trailheads(elev_map=elev_map, headings=headings, elev0_set=elev0_set)
    return sum([len(s) for th, s in t_heads.items()])


def calc_day10b(topo_map: list[str]) -> int:
    elev_map = parse_topo_map(topo_map)
    elev0_set = find_elevs(elev_map=elev_map, target_elev=0)
    headings = find_headings(elev_map=elev_map)
    all_trails = find_all_trails_trailhead(elev_map=elev_map, headings=headings, elev0_set=elev0_set)
    return sum([len(s) for tr_set, s in all_trails.items()])

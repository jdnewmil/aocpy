"""AOC 2024 Day05 functions."""

import re
from typing import Optional, TypeAlias
import graphlib as gl
from . import day03

UP: int = 0
RIGHT: int = 1
DOWN: int = 2
LEFT: int = 3

guard_dirs = '^>v<'

GuardDir: TypeAlias = tuple[int, int, int]
GuardLoc: TypeAlias = tuple[int, int]

OUTSIDE: GuardDir = (-1, -1, -1)


def find_guard(grid_room: list[str]) -> Optional[GuardDir]:
    j = 0
    gpat = re.compile(r'([\^>v<])')
    while j < len(grid_room):
        row = grid_room[j]
        match = re.search(gpat, row)
        if match:
            return match.start(), j, guard_dirs.index(match.group(1))
        j += 1
    return None


def turn_guard_right(loc: GuardDir) -> GuardDir:
    return loc[0], loc[1], (loc[2] + 1) % 4


def guard_will_bump(grid_room: list[str], loc: GuardDir) -> Optional[GuardDir]:
    """Return None if will bump, return incremented loc otherwise.

    Parameters
    ----------
    grid_room : list[str]
        Map of room with '.' or a guard character as open space.
    loc : GuardDir
        Tuple of i,j and direction.

    Returns
    -------
    Optional[GuardDir]
        None if would bump, OUTSIDE if would exit map, or
        incremented location otherwise.
    """
    i_bounds = [-1, len(grid_room[0])]
    j_bounds = [-1, len(grid_room)]
    next_loc = guard_loc_increment(grid_room=grid_room, loc=loc)
    free_loc_chars = '.' + guard_dirs
    if loc[2] % 2:
        # right/left
        if next_loc[0] in i_bounds:
            return OUTSIDE
        if grid_room[next_loc[1]][next_loc[0]] not in free_loc_chars:
            return None
        return next_loc
    if next_loc[1] in j_bounds:
        return OUTSIDE
    if grid_room[next_loc[1]][next_loc[0]] not in free_loc_chars:
        return None
    return next_loc


def guard_loc_increment(grid_room: list[str], loc: GuardDir) -> GuardDir:
    i_inc = (1, -1)
    j_inc = (-1, 1)
    if loc[2] % 2:
        # right/left
        return loc[0] + i_inc[loc[2] // 2], loc[1], loc[2]
    # up/down
    return loc[0], loc[1] + j_inc[loc[2] // 2], loc[2]


def map_guard_trail(grid_room: list[str], init_loc: GuardDir) -> set[GuardDir]:
    result = set()
    loc = init_loc
    while True:
        result.add(loc)
        next_loc = guard_will_bump(grid_room=grid_room, loc=loc)
        if next_loc in result:
            raise ValueError("Loop")
        if OUTSIDE == next_loc:
            return result
        if next_loc is not None:
            loc = next_loc
        else:
            loc = turn_guard_right(loc)
    return result

def get_positions(trail_set: set[GuardDir]) -> set[GuardLoc]:
    return set(
        [
            (i, j)
            for i, j, dir in trail_set])

def positions_set_to_map(
    grid_room: list[str]
    , positions: set[GuardLoc]
    , mark: str = 'X'
) -> list[str]:
    return [  # new list of strings
        ''.join(  # pack new list of characters
            [
                mark
                if (i, j) in positions
                else c
                for i, c in enumerate(row)])
        for j, row in enumerate(grid_room)]


def find_loop_positions(grid_room: list[str], init_loc: GuardDir) -> set[GuardLoc]:
    trail = map_guard_trail(grid_room, init_loc=init_loc)
    trail.remove(init_loc)
    possible_pos = get_positions(trail_set=trail)
    loop_set = set()
    for pos in possible_pos:
        temp_map = positions_set_to_map(
            grid_room=grid_room
            , positions=set([pos])
            , mark = '#')
        try:
            trail = map_guard_trail(temp_map, init_loc) # type: ignore
        except:
            loop_set.add(pos)
    return loop_set
        

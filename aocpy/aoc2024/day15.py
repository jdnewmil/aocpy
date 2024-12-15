"""AOC 2024 Day15 functions."""

from typing import TypeAlias, Self
from dataclasses import dataclass
from . import day13

RawLoc: TypeAlias = tuple[int, int]
RawStep: TypeAlias = tuple[int, int]
RobotMap: TypeAlias = list[list[str]]
RobotDictMap: TypeAlias = tuple[RawLoc, RawLoc, dict[str, set[RawLoc]]]
    # rpos, dims, objpos_dict
RawLocList: TypeAlias = list[RawLoc]
RawStepList: TypeAlias = list[RawStep]

ROBOT: str = '@'
WALL: str = '#'
BOX: str = 'O'
OPEN: str = '.'

OUTSIDE: RawLoc = (-1, -1)

IDIR: int = 0
JDIR: int = 1

# (dimension, increment)
UP: RawStep = (JDIR, -1)
RIGHT: RawStep = (IDIR, 1)
DOWN: RawStep = (JDIR, 1)
LEFT: RawStep = (IDIR, -1)


move_map: dict[str, RawStep] = {
    '^': UP
    , '>': RIGHT
    , 'v': DOWN
    , '<': LEFT}


def parse_file(lns: list[str]) -> tuple[RobotMap,RawStepList]:
    map_move_lns = day13.split_list_at_value(lns)
    map = [
        [
            c
            for c in row]
        for row in map_move_lns[0]]
    move_str = ''.join(map_move_lns[1])
    move_list = [
        move_map[m]
        for m in move_str]
    return map, move_list


def rmap_to_rdm(rmap: RobotMap) -> RobotDictMap:
    result = {
        WALL: set()
        , BOX: set()}
    rpos = OUTSIDE
    for j, row in enumerate(rmap):
        for i, c in enumerate(row):
            if ROBOT == c:
                rpos = (i, j)
            elif OPEN != c:
                result[c].add((i, j))
    return rpos, (len(rmap[0]), len(rmap)), result


def rdm_to_rmap(rdm: RobotDictMap) -> RobotMap:
    rpos, rdims, rdict = rdm
    rmap = [
        [
            OPEN
            for i in range(rdims[IDIR])]
        for j in range(rdims[JDIR])]
    for objtype, pos_set in rdict.items():
        for i, j in pos_set:
            rmap[j][i] = objtype
    rmap[rpos[JDIR]][rpos[IDIR]] = ROBOT
    return rmap


def print_rmap(rmap: RobotMap):
    for row in rmap:
        print(''.join(row))


def inc(rpos: RawLoc, mv: RawStep) -> RawLoc:
    dimension, increment = mv
    if dimension:  # JDIR
        return (rpos[0], rpos[1] + increment)
    return (rpos[0] + increment, rpos[1])


def move_robot(rdm: RobotDictMap, mv: RawStep) -> RobotDictMap:
    rpos, rdims, rdict = rdm
    # deal with objects in the way
    boxes = []
    p = rpos
    while True:
        p = inc(rpos=p, mv=mv)
        if p in rdict[BOX]:
            boxes.append(p)
        else:
            break
    blocked = p in rdict[WALL]
    if not blocked:
        if len(boxes):
            rdict[BOX].add(p)
            rdict[BOX].remove(boxes[0])
            rpos = boxes[0]
        else:
            rpos = p        
    return rpos, rdims, rdict

def do_robot_moves(rdm: RobotDictMap, mv_list: RawStepList) -> RobotDictMap:
    result = rdm
    for mv in mv_list:
        result = move_robot(result, mv)
    return result

def calc_gps_coordinate(pos: RawLoc) -> int:
    return 100 * pos[JDIR] + pos[IDIR]

def calc_gps_score(rdm: RobotDictMap) -> int:
    rpos, dims, rdict = rdm
    return sum(
        [
            calc_gps_coordinate(p)
            for p in rdict[BOX]])

def calc_day15a(lns: list[str]) -> int:
    rmap, rmoves = parse_file(lns)
    rdm = rmap_to_rdm(rmap=rmap)
    rdm = do_robot_moves(rdm, rmoves)
    return calc_gps_score(rdm)

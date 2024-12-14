"""AOC 2024 Day14 functions."""

from typing import TypeAlias, Self
from dataclasses import dataclass
import re

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

    def __mod__(self, y) -> Self:
        return IntVec(
            value=(
                self.value[0] % y.value[0]
                , self.value[1] % y.value[1])) # type: ignore


@dataclass
class Robot:
    p: IntVec
    v: IntVec

    def move(self, field_dim: IntVec) -> Self:
        return Robot(
            p=(self.p + self.v) % field_dim
            , v=self.v) # type: ignore


def parse_robot(ln: str, pat: re.Pattern) -> Robot:
    match = pat.match(ln)
    if not match:
        raise ValueError(f'could not parse {ln}')
    return Robot(
        p=IntVec(
            value=(
                int(match.group(1))
                , int(match.group(2))))
        , v=IntVec(
            value=(
                int(match.group(3))
                , int(match.group(4)))))


def parse_robots_data(lns: list[str]) -> list[Robot]:
    pat = re.compile(r'p=(\d+), *(\d+) *v=([+-]?\d+), *([+-]?\d+)')
    return [
        parse_robot(ln, pat=pat)
        for ln in lns]


def map_robots_list(rlist: list[Robot], field_dim: IntVec) -> list[list[int]]:
    result = [[0] * field_dim.value[0] for i in range(field_dim.value[1])]
    for r in rlist:
        result[r.p.value[1]][r.p.value[0]] += 1
    return result


def step_robots_list(rlist: list[Robot], field_dim: IntVec) -> list[Robot]:
    return [
        r.move(field_dim=field_dim)
        for r in rlist]

def run_robots_list(
    rlist: list[Robot]
    , steps: int
    , field_dim: IntVec
) -> list[Robot]:
    result = rlist
    for i in range(steps):
        result = step_robots_list(result, field_dim=field_dim)
    return result


def split_dim(v: int, vq: tuple[int, int], vp: int, field_size: int) -> int:
    if vq[1]:
        if v < vq[0] and 0 <= v:
            return 0
        elif vq[0] < v and v < field_size:
            return 1
        else:
            return -1
    else:
        if v < vq[0] and 0 <= v:
            return 0
        elif vq[0] <= v and v < field_size:
            return 1
        else:
            return -1
        

def product(v: list[int]) -> int:
    result = 1
    for i in v:
        result *= i
    return result


def calc_qscores(rlist: list[Robot], field_dim: IntVec) -> list[list[int]]:
    xq = divmod(field_dim.value[0], 2)
    yq = divmod(field_dim.value[1], 2)
    xp = sum(xq)
    yp = sum(yq)
    qscores = [[0, 0], [0, 0]]
    for r in rlist:
        x, y = r.p.value
        x0 = split_dim(v=x, vq=xq, vp=xp, field_size=field_dim.value[0])
        if x0 < 0:
            continue
        y0 = split_dim(v=y, vq=yq, vp=yp, field_size=field_dim.value[1])
        if y0 < 0:
            continue
        qscores[y0][x0] += 1
    return qscores


def calc_safety_factor(rlist: list[Robot], field_dim: IntVec) -> int:
    qscores = calc_qscores(rlist, field_dim)
    return product(
        [
            product(row)
            for row in qscores])


def calc_day14a(lns: list[str], field_dim: IntVec) -> int:
    rlist = parse_robots_data(lns)
    result = run_robots_list(rlist, 100, field_dim=field_dim)
    return calc_safety_factor(rlist=result, field_dim=field_dim)


def print_robots_map(rm: list[list[int]]):
    for row in rm:
        print(
            ''.join(
                [
                    str(i)
                    if 0 < i
                    else ' '
                    for i in row]))


def print_step_rlist(step_rlist: tuple[int, list[Robot]], field_dim: IntVec):
    step, rlist = step_rlist
    rm = map_robots_list(rlist, field_dim=field_dim)
    print('=' * 20 + f' {step} ' + '=' * 50)
    print_robots_map(rm)


def seek_symmetric_qscores(
    step_rlist: tuple[int,list[Robot]]
    , field_dim: IntVec
    , tolerance: int
) -> tuple[int,list[Robot]]:
    step, result = step_rlist
    while True:
        result = step_robots_list(result, field_dim=field_dim)
        step += 1
        qscores = calc_qscores(rlist=result, field_dim=field_dim)
        if (
            abs(qscores[0][1] - qscores[0][0]) <= tolerance
            and abs(qscores[1][1] - qscores[1][0]) <= tolerance
        ):
            return step, result

def calc_neighbored(rlist: list[Robot]) -> int:
    pos_set = set((
        r.p.value
        for r in rlist
    ))
    def neighbored(p: tuple[int, int]) -> bool:
        return (
            (p[0] - 1,    p[1]) in pos_set
            or (p[0] - 1, p[1] + 1) in pos_set
            or (p[0],     p[1] + 1) in pos_set
            or (p[0] + 1, p[1] + 1) in pos_set
            or (p[0] + 1, p[1]) in pos_set
            or (p[0] + 1, p[1] - 1) in pos_set
            or (p[0],     p[1] - 1) in pos_set
            or (p[0] - 1, p[1] - 1) in pos_set)
    return sum(
        (
            neighbored(r.p.value)
            for r in rlist))


def seek_neighborly_robots(
    step_rlist: tuple[int,list[Robot]]
    , field_dim: IntVec
    , tolerance: int
) -> tuple[int,list[Robot]]:
    step, result = step_rlist
    n_max = len(result)
    while True:
        result = step_robots_list(result, field_dim=field_dim)
        step += 1
        n = calc_neighbored(result)
        if (n_max - n) < tolerance:
            return step, result


def do_day14b(step_rlist: tuple[int,list[Robot]], field_dim: IntVec, tolerance: int):
    result = seek_neighborly_robots(
        step_rlist
        , field_dim=field_dim
        , tolerance=tolerance)
    print_step_rlist(result, field_dim=field_dim)
    return result

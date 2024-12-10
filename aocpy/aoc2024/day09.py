"""AOC 2024 Day09 functions."""

from typing import Optional, TypeAlias, Callable, Self
from dataclasses import dataclass
from itertools import permutations

FREE: int = -1

def expand_disk_map(disk_map: str) -> tuple[list[int], int]:
    result = []
    for i, c in enumerate(disk_map):
        n = int(c)
        if i % 2:
            result.extend([FREE] * n)
        else:
            fnum = i // 2
            result.extend([fnum] * n)
    return result, fnum


def seek_free_index(exp_disk_map: list[int], start: int, end: int) -> int:
    while start < end:
        if FREE == exp_disk_map[start]:
            return start
        start += 1
    return -1  # all free space is after end pointer


def seek_nonfree_index(
    exp_disk_map: list[int]
    , start: int
    , end: int
) -> int:
    while start < end:
        if FREE != exp_disk_map[end]:
            return end
        end -= 1
    return -1
            

def compact_expanded_map(exp_disk_map: list[int]) -> list[int]:
    start = 0
    end = len(exp_disk_map) - 1
    result = exp_disk_map.copy()
    while True:
        end = seek_nonfree_index(
            exp_disk_map=result, start=start, end=end)
        if end < 0:
            return result
        start = seek_free_index(
            exp_disk_map=result, start=start, end=end)
        if start < 0:
            return result
        result[start] = result[end]
        result[end] = FREE

def find_fblk(dm: list[tuple[int, int]], flen: int, end_blk: int) -> int:
    result = 1
    while result < end_blk:
        dest_num, dest_len = dm[result]
        if FREE == dest_num and flen <= dest_len:
            return result
        result += 1
    return -1


def compact_disk_map_b(disk_map: str) -> list[int]:
    dm = []
    for i, c in enumerate(disk_map):
        n = int(c)
        if 0 < n:
            if i % 2:
                fnum = FREE
            else:
                fnum = i // 2
            dm.append((fnum, n))
    blk = len(dm) - 1
    while 0 < blk:
        file_num, file_len = dm[blk]
        if FREE != file_num:
            free_blk = find_fblk(dm, file_len, end_blk=blk)
            if 0 < free_blk:  # suitable free block found?
                free_len = dm[free_blk][1]
                if file_len < free_len:  # need to split free block
                    dm = (
                        dm[0:free_blk]
                        + [(file_num, file_len)]
                        + [(FREE, free_len - file_len)]
                        + dm[(free_blk + 1):blk]
                        + [(FREE, file_len)]
                        + dm[(blk + 1):])
                    blk += 1
                else:  # swap free block and file block
                    dm = (
                        dm[0:free_blk]
                        + [(file_num, file_len)]
                        + dm[(free_blk + 1):blk]
                        + [(FREE, file_len)]
                        + dm[(blk + 1):])
        blk -= 1
    result = []
    idx = 1
    for fnum, flen in dm:
        result.extend([fnum] * flen)
    return result


def calc_checksum(exp_disk_map: list[int]) -> int:
    result = 0
    for i, v in enumerate(exp_disk_map):
        if 0 <= v:
            result += i * v
    return result


def calc_day09a(disk_map: str) -> int:
    edm = expand_disk_map(disk_map)[0]
    edm1 = compact_expanded_map(edm)
    return calc_checksum(edm1)

def calc_day09b(disk_map: str) -> int:
    edm = compact_disk_map_b(disk_map)
    return calc_checksum(edm)


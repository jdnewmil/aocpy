"""AOC 2024 Day05 functions."""

from typing import Optional, TypeAlias
import graphlib as gl
from . import day03

def build_sorted(rules: list[tuple[int, int]]) -> list[int]:
    ts = gl.TopologicalSorter(dict())
    for rule in rules:
        ts.add(rule[1], rule[0])
    return list(ts.static_order())


def build_so_map(so: list[int]) -> dict[int, int]:
    return {
        n: i
        for i, n in enumerate(so)}


def update_is_sorted(update: list[int], som: dict[int, int]) -> bool:
    i = som[update[0]]
    for n in update[1:]:
        i_next = som[n]
        if i_next < i:
            return False
        i = i_next
    return True


def read_rules_updates(fname: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    lns = day03.read_lines(fname=fname)
    i_brk = lns.index('')
    rules = [
        tuple([
            int(sn)
            for sn in ln.split('|')
        ])
        for ln in lns[:i_brk]]
    updates = [
        [
            int(sn)
            for sn in ln.split(',')
        ]
        for ln in lns[i_brk+1:]
    ]
    return rules, updates


def calc_day05a(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    result = 0
    for update in updates:
        frules = [
            r
            for r in rules
            if r[0] in update and r[1] in update]
        so = build_sorted(frules)
        som = build_so_map(so)
        if update_is_sorted(update, som):
            mid = len(update) // 2
            result += update[mid]
    return result


def calc_day05b(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    result = 0
    for update in updates:
        frules = [
            r
            for r in rules
            if r[0] in update and r[1] in update]
        so = build_sorted(frules)
        som = build_so_map(so)
        if not update_is_sorted(update, som):
            mid = len(update) // 2
            result += so[mid]
    return result

"""AOC 2024 Day01 functions."""

def pairsort1(l1: list[int], l2: list[int]) -> tuple[list[int], list[int]]:
    result1 = l1.copy()
    result1.sort()
    result2 = l2.copy()
    result2.sort()
    return result1, result2

def diff1(l1s: list[int], l2s: list[int]) -> list[int]:
    return [
        abs(v2 - v1)
        for v1, v2 in zip(l1s, l2s)]

def similarity1(l1s: list[int], l2s: list[int]) -> list[int]:
    d = dict()
    for l2 in l2s:
        if l2 in d:
            d[l2] += 1
        else:
            d[l2] = 1
    return [
        l1 * d[l1]
        if l1 in d
        else 0
        for l1 in l1s]

"""AOC 2024 Day11 functions."""

from typing import Callable, TypeAlias

StoneBlink: TypeAlias = list[int]
StoneBlinkD: TypeAlias = dict[int, int]  # stone_value, count
StoneBlinks: TypeAlias = dict[int, StoneBlink]
StoneCache: TypeAlias = dict[int, StoneBlinks]
BlinkFun: TypeAlias = Callable[[int], list[int]]


def parse_stones(ln: str) -> StoneBlink:
    return [int(s) for s in ln.split(' ')]


def to_stone_blinkd(sb: StoneBlink) -> StoneBlinkD:
    result = {}
    for i in sb:
        incd(i, 1, result)
    return result


def incd(i: int, n: int, cache: StoneBlinkD):
    if i in cache:
        cache[i] += n
    else:
        cache[i] = n


def blinkd(i: int, n: int, cache: StoneBlinkD):
    if 0 == i:
        incd(1, n, cache)
    else:
        s = str(i)
        m = len(s)
        if m % 2:
            incd(i * 2024, n, cache)
        else:
            m2 = m // 2
            incd(int(s[:m2]), n, cache)
            incd(int(s[m2:]), n, cache)


def blinkds(cache: StoneBlinkD) -> StoneBlinkD:
    result = {}
    for sv, cnt in cache.items():
        blinkd(sv, cnt, result)
    return result


def blink1(i: int) -> StoneBlink:
    if 0 == i:
        return [1]
    else:
        s = str(i)
        m = len(s)
        if m % 2:
            return [i * 2024]
        m2 = m // 2
        return [int(s[:m2]), int(s[m2:])]


def int2digits(i: int) -> list[int]:
    result = []
    while 9 < i:
        result.append(i % 10)
        i = i // 10
    result.append(i)
    return result


def int_split2(i: int) -> list[int]:
    digits = int2digits(i)
    n = len(digits)
    n2 = n // 2 - 1
    result1 = 0
    for k in range(n - 1, n2):
        result1 = 10 * result1 + k
    result2 = 0
    for k in range(n2, -1, -1):
        result2 = 10 * result2 + k
    return [result1, result2]


def blink1b(i: int) -> StoneBlink:
    if 0 == i:
        return [1]
    else:
        digits = int2digits(i)
        n = len(digits)
        if n % 2:
            return [i * 2024]
        n2 = n // 2 - 1
        result1 = 0
        for k in range(n - 1, n2, -1):
            result1 = 10 * result1 + digits[k]
        result2 = 0
        for k in range(n2, -1, -1):
            result2 = 10 * result2 + digits[k]
        return [result1, result2]


def blink(
    cur: list[int]
    , fn1: BlinkFun = blink1
) -> list[int]:
    result = []
    for i in cur:
        result.extend(fn1(i))
    return result


def blinks(
    cur: list[int]
    , n: int
    , fn1: Callable[[int], list[int]] = blink1
) -> list[int]:
    result = cur.copy()
    for k in range(n):
        result = blink(result, fn1=fn1)
    return result

def blinkdsn(cache: StoneBlinkD, n_steps: int) -> StoneBlinkD:
    result = cache.copy()
    for i in range(n_steps):
        result = blinkds(result)
    return result


def count_stone_blinkd(cache: StoneBlinkD) -> int:
    return sum(cache.values())


def calc_day11a(ln: str, n: int = 25) -> int:
    stones = parse_stones(ln)
    return len(blinks(stones, n))


def calc_day11b(ln: str, n: int = 25) -> int:
    stones = parse_stones(ln)
    cache = to_stone_blinkd(stones)
    result = blinkdsn(cache, n)
    return count_stone_blinkd(result)

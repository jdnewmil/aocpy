"""AOC 2024 Day02 functions."""

def diffl(v: list[int]) -> list[int]:
    return [
        e2 - e1
        for e1, e2 in zip(v[:len(v)], v[1:])]


def absl(v: list[int]) -> list[int]:
    return [
        abs(e)
        for e in v]


def rangel(v: list[int]) -> tuple[int, int]:
    rmin = rmax = v[0]
    for e in v[1:]:
        if e < rmin:
            rmin = e
        elif rmax < e:
            rmax = e
    return rmin, rmax


def sgnl(v: list[int]) -> list[int]:
    def sgn(e: int) -> int:
        if 0 == e:
            return 0
        elif e < 0:
            return -1
        return 1
    return [
        sgn(e)
        for e in v]


def alleq(v: list[int]) -> bool:
    result = True
    ref = v[0]
    for e in v[1:]:
        if e != ref:
            return False
    return True


def is_safe(v: list[int]) -> bool:
    d = diffl(v)
    ad = absl(d)
    mn, mx = rangel(ad)
    sd = sgnl(d)
    is_monotonic = alleq(sd) and 0 != sd[0]
    return 1 <= mn and mx <= 3 and is_monotonic


def is_anydrop_safe(v: list[int]) -> bool:
    for i, e in enumerate(v):
        v0 = v.copy()
        del(v0[i])
        if is_safe(v0):
            return True
    return False


def parse_int_row(ln: str, sep=' ') -> list[int]:
    sa = ln.split(sep)
    return [
        int(e)
        for e in sa]


def read_int_rows(fname: str) -> list[list[int]]:
    with open(fname, 'r') as f:
        sl = f.readlines()
    return [
        parse_int_row(ln.strip())
        for ln in sl]

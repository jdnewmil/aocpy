"""AOC 2024 Day13 functions."""

from typing import TypeAlias, Optional
from dataclasses import dataclass
import re

RawVec: TypeAlias = tuple[int, int]
Buttons: TypeAlias = dict[str, RawVec]

@dataclass
class ClawMachine:
    buttons: Buttons
    prize: RawVec
    price: RawVec
    max_presses: Optional[int]

    def solve(self) -> RawVec:
        A = (self.buttons['A'], self.buttons['B'])
        b = self.prize
        # a_11 * x_1 + a_12 * x_2 = b_1
        # a_21 * x_1 + a_22 * x_2 = b_2
        #
        # det = a_12 * a_21 - a_11 * a_22
        # num_1 = a_12 * b_2 - a_22 * b_1
        # num_2 = a_21 * b_1 - a_11 * b_2
        # x_1 = num_1 / det
        # x_2 = num_2 / det
        det = A[1][0] * A[0][1] - A[0][0] * A[1][1]
        num_1 = A[1][0] * b[1] - A[1][1] * b[0]
        num_2 = A[0][1] * b[0] - A[0][0] * b[1]
        if 0 == det:   # collinearity
            btnAx = divmod(b[0], A[0][0])
            btnAy = divmod(b[1], A[0][1])
            btnBx = divmod(b[0], A[1][0])
            btnBy = divmod(b[1], A[1][1])
            # if not divisible by Button A
            if btnAx[1] or btnAy[1]:
                # might still be divisible by Button B
                if btnBx[1] or btnBy[1]:
                    return (0, 0)
                # check that same divisor works for button B Y coord
                if btnBx[0] != btnBy[0]:
                    return (0, 0)
                return (0, btnBx[0])
            elif btnBx[1] or btnBy[1]:
                # btnA could work, btnB does not
                if btnAx[0] != btnAy[0]:
                    return (0, 0)
                return (btnBx[0], 0)
            if btnAx[0] != btnAy[0]:
                if btnBx[0] != btnBy[0]:
                    return (0, 0)
                return (0, btnBx[0])
            cost_x = self.price[0] * btnAx[0]
            cost_y = self.price[1] * btnBx[0]
            if cost_x < cost_y:
                return (btnAx[0], 0)
            return (0, btnBx[0])
        x = divmod(num_1, det)
        y = divmod(num_2, det)
        if x[1] or y[1]:
            return (0, 0)
        result = (x[0], y[0])
        if self.max_presses is not None:
            if 100 < result[0] or 100 < result[1]:
                return (0, 0)
        return result


def parse_claw_machine(
    lns: list[str]
    , price=(3, 1)
    , offset=0
    , max_presses: Optional[int] = 100
) -> ClawMachine:
    buttons = dict()
    prize = None
    button_pat = re.compile(r'Button +(.): +X\+(\d+), Y\+(\d+)')
    prize_pat = re.compile(r'Prize: +X\=(\d+), Y\=(\d+)')
    for ln in lns:
        match = button_pat.match(ln)
        if match:
            buttons[match.group(1)] = (
                int(match.group(2)) # type: ignore
                , int(match.group(3))) # type: ignore
        elif match := prize_pat.match(ln):
            prize = (
                int(match.group(1)) + offset # type: ignore
                , int(match.group(2)) + offset) # type: ignore
    if prize is None:
        raise ValueError('Missing Prize line')
    if 0 == len(buttons):
        raise ValueError('Missing any Buttons lines')
    return ClawMachine(buttons=buttons, prize=prize, price=price, max_presses=max_presses)


def split_list_at_value(lns: list[str], sep='') -> list[list[str]]:
    result = []
    accum = []
    for ln in lns:
        if '' == ln:
            if 0 == len(accum):
                continue
            result.append(accum)
            accum = []
        else:
            accum.append(ln)
    if 0 < len(accum):
        result.append(accum)
    return result


def parse_claw_machines(
    lns_list: list[list[str]]
    , offset=0
    , max_presses: Optional[int] = 100
) -> list[ClawMachine]:
    return [
        parse_claw_machine(lns, offset=offset, max_presses=max_presses)
        for lns in lns_list]


def solve_claw_machines(cms: list[ClawMachine]) -> list[RawVec]:
    return [
        cm.solve()
        for cm in cms]

def calc_day13a(lns: list[str]) -> int:
    lns_list = split_list_at_value(lns)
    cms = parse_claw_machines(lns_list)
    solns = solve_claw_machines(cms)
    return sum(
        [
            3 * s[0] + s[1]
            for s in solns])


def calc_day13b(lns: list[str]) -> int:
    lns_list = split_list_at_value(lns)
    cms = parse_claw_machines(
        lns_list
        , offset=10000000000000
        , max_presses=None)
    solns = solve_claw_machines(cms)
    return sum(
        [
            3 * s[0] + s[1]
            for s in solns])

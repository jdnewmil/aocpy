"""AOC 2024 Day07 functions."""

from typing import Optional, TypeAlias, Callable
from itertools import product

EquationValues : TypeAlias = tuple[int, list[int]]


def plus(stack: list[int]) -> list[int]:
    x = stack.pop()
    y = stack.pop()
    stack.append(x + y)
    return stack


def mul(stack: list[int]) -> list[int]:
    x = stack.pop()
    y = stack.pop()
    stack.append(x * y)
    return stack
    

def concat(stack: list[int]) -> list[int]:
    x = stack.pop()
    y = stack.pop()
    stack.append(int(str(x) + str(y)))
    return stack


def parse_eqn_values(ln: str) -> EquationValues:
    left_right = ln.split(':')
    nums = left_right[1].split()
    return int(left_right[0]), [int(ns) for ns in nums]


def parse_all_eqn_values(lns: list[str]) -> list[EquationValues]:
    return [
        parse_eqn_values(ln)
        for ln in lns]


def check_eqn(
    eqn_values: EquationValues
    , oplist: tuple[str, ...]
    , opset: dict[str, Callable]
) -> bool:
    given_result, values = eqn_values
    stack = values[::-1]  # reversed list
    assert len(stack) == (1 + len(oplist))
    for opstr in oplist:
        stack = opset[opstr](stack)
    return given_result == stack.pop()


def check_eqn_op_combos(
    eqn_values: EquationValues
    , opset: dict[str, Callable]
) -> bool:
    ops = list(opset.keys())
    for combo in product(ops, repeat=len(eqn_values[1]) - 1):
        if check_eqn(
            eqn_values=eqn_values
            , oplist=combo
            , opset=opset
        ):
            return True
    return False

def calc_day07a(
    eqn_values: list[EquationValues]
    , opset: dict[str, Callable]
) -> int:
    result = 0
    for eqv in eqn_values:
        if check_eqn_op_combos(eqn_values=eqv, opset=opset):
            result += eqv[0]
    return result


"""AOC 2024 Day 7 test code."""

import pytest
from .. import day07

@pytest.fixture
def sample07() -> list[str]:
    eqn_values = [
        "190: 10 19"
        , "3267: 81 40 27"
        , "83: 17 5"
        , "156: 15 6"
        , "7290: 6 8 6 15"
        , "161011: 16 10 13"
        , "192: 17 8 14"
        , "21037: 9 7 18 13"
        , "292: 11 6 16 20"]
    return eqn_values


def test_day07a(sample07):
    ans = day07.parse_eqn_values(sample07[0])
    assert 190 == ans[0]
    assert [10, 19] == ans[1]
    opset = {
        '*': day07.mul
        , '+': day07.plus}
    assert day07.check_eqn(ans, ('*',), opset)
    assert not day07.check_eqn(ans, ('+',), opset)
    assert day07.check_eqn_op_combos(ans, opset=opset)
    eqn_values = day07.parse_all_eqn_values(sample07)
    assert day07.check_eqn_op_combos(eqn_values[1], opset=opset)
    assert not day07.check_eqn_op_combos(eqn_values[2], opset=opset)
    assert day07.check_eqn_op_combos(eqn_values[8], opset=opset)
    assert 3749 == day07.calc_day07a(eqn_values=eqn_values, opset=opset)


def test_day07b(sample07):
    eqn_values = day07.parse_all_eqn_values(sample07)
    opset = {
        '*': day07.mul
        , '+': day07.plus
        , '||': day07.concat}
    assert 11387 == day07.calc_day07a(eqn_values=eqn_values, opset=opset)

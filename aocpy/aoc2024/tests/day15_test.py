"""AOC 2024 Day 15 test code."""

import pytest
from .. import day15


@pytest.fixture
def sample15_1() -> list[str]:
    lns = [
        '##########'
        , '#..O..O.O#'
        , '#......O.#'
        , '#.OO..O.O#'
        , '#..O@..O.#'
        , '#O#..O...#'
        , '#O..O..O.#'
        , '#.OO.O.OO#'
        , '#....O...#'
        , '##########'
        , ''
        , '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^'
        , 'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v'
        , '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<'
        , '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^'
        , '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><'
        , '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^'
        , '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^'
        , '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>'
        , '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>'
        , 'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^']
    return lns


@pytest.fixture
def sample15_2() -> list[str]:
    lns = [
        '########'
        , '#..O.O.#'
        , '##@.O..#'
        , '#...O..#'
        , '#.#.O..#'
        , '#...O..#'
        , '#......#'
        , '########'
        , ''
        , '<^^>>>vv<v>>v<<']
    return lns


def test_day15a(sample15_1, sample15_2):
    rmap2, rmoves2 = day15.parse_file(sample15_2)
    rdm2 = day15.rmap_to_rdm(rmap=rmap2)
    rdm2_1 = day15.move_robot(rdm2, rmoves2[0])
    # day15.print_rmap(day15.rdm_to_rmap(rdm2_1))
    rdm2_n = day15.do_robot_moves(rdm2_1, rmoves2[1:])
    # day15.print_rmap(day15.rdm_to_rmap(rdm2_n))
    assert day15.rdm_to_rmap(rdm2_n) == [
        ['#', '#', '#', '#', '#', '#', '#', '#']
        , ['#', '.', '.', '.', '.', 'O', 'O', '#']
        , ['#', '#', '.', '.', '.', '.', '.', '#']
        , ['#', '.', '.', '.', '.', '.', 'O', '#']
        , ['#', '.', '#', 'O', '@', '.', '.', '#']
        , ['#', '.', '.', '.', 'O', '.', '.', '#']
        , ['#', '.', '.', '.', 'O', '.', '.', '#']
        , ['#', '#', '#', '#', '#', '#', '#', '#']]
    assert 2028 == day15.calc_day15a(sample15_2)
    assert 10092 == day15.calc_day15a(sample15_1)


def test_day15b(sample15_1):
    assert False

    
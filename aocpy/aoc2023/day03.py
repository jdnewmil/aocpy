# day03.py
"""Computation for 2023 day 3"""


def find_numbers_03a(mp: list[str]) -> set[tuple]:
    """Find number positions tuples for all numbers in the map mp.

    Parameters
    ----------
    mp : list[str]
        List of strings representing rows in map

    Returns
    -------
    set[tuple]
        Set of number position tuples contining numbers in the map.
    """
    result = set()
    for rowidx, row in enumerate(mp):
        isdigit_last = False
        for colidx, v in enumerate(row):
            if v.isdigit():
                if not isdigit_last:
                    leftidx = colidx
                isdigit_last = True
            elif isdigit_last:
                result.add((rowidx, leftidx, colidx))
                isdigit_last = False
        if isdigit_last:
            result.add((rowidx, leftidx, len(row)))
    return result


def get_numberpos_left(row: str, start_coord: tuple[int]) -> tuple[int]:
    """Identify the number position coordinates to the left of a digit.

    Positions are searched only to the left of start_coord.

    Parameters
    ----------
    row : str
        Map row to search.
    start_coord : tuple[int]
        Tuple of two integers (row, col) indicating the coordinate containing
        a digit that is only expected to have adjacent digits to the left.

    Returns
    -------
    tuple[int]
        _description_
    """
    col = start_coord[1]
    if 0 < col:
        col -= 1
        while 0 <= col and row[col].isdigit():
            col -= 1
        col += 1
    return (start_coord[0], col, start_coord[1] + 1)


def get_numberpos_right(row: str, start_coord: tuple[int]) -> tuple[int]:
    """Identify the number position coordinates to the right of a digit.

    Positions are searched only to the right of start_coord.

    Parameters
    ----------
    row : str
        Map row to search.
    start_coord : tuple[int]
        Tuple of two integers (row, col) indicating the coordinate containing
        a digit that is only expected to have adjacent digits to the right.

    Returns
    -------
    tuple[int]
        Number position tuple (row, start, stop)
    """
    col = start_coord[1] + 1
    mapwidth = len(row)
    while col < mapwidth and row[col].isdigit():
        col += 1
    return (start_coord[0], start_coord[1], col)


def get_numberpos_mid(row: str, start_coord: tuple[int]) -> tuple[int]:
    """Identify the number position coordinates given a coordinate with a digit.

    Positions are searched left and right to account for all digits.

    Parameters
    ----------
    row : str
        Map row to search.
    start_coord : tuple[int]
        Tuple of two integers (row, col) indicating the coordinate containing
        a digit that may have adjacent digits in both directions.

    Returns
    -------
    tuple[int]
        Number position tuple (row, start, stop)
    """
    start_col = start_coord[1]
    if 0 < start_col:
        start_col -= 1
        while 0 <= start_col and row[start_col].isdigit():
            start_col -= 1
        start_col += 1
    col = start_coord[1] + 1
    mapwidth = len(row)
    while col < mapwidth and row[col].isdigit():
        col += 1
    return (start_coord[0], start_col, col)


def is_symbol(s: str) -> bool:
    """Test if length one string is a symbol.

    Parameters
    ----------
    s : str
        String with length 1.

    Returns
    -------
    bool
        True if it is a symbol, False otherwise.
    """
    return not (s.isdigit() or '.' == s)


def is_star(s: str) -> bool:
    """Test if length one string is a gear.

    Parameters
    ----------
    s : str
        String with length 1.

    Returns
    -------
    bool
        True if it is a gear (asterisk), False otherwise.
    """
    return '*' == s


def check_adjacent(mp: list[str], numberpos: tuple) -> bool:
    """Check for symbols in locations "adjacent" to numberpos.

    Parameters
    ----------
    mp : list[str]
        List of strings representing rows in map
    numberpos : tuple
        Triplet:
        0: row number
        1: position of leftmost digit in number
        2: position of character after leftmost digit in number

    Returns
    -------
    bool
        True if there is at least one symbol adjacent to the number.
    """
    mapwidth = len(mp[0])
    mapheight = len(mp)
    # first column index of adjacency positions
    left = max(0, numberpos[1] - 1)
    # one past last index of adjacenzy positions
    right = min(mapwidth, numberpos[2] + 1)
    # row above
    if 0 < numberpos[0]:  # skip if digits on first row
        row = mp[numberpos[0] - 1]
        for col in range(left, right):
            if is_symbol(row[col]):
                return True
    # row of number, left end
    row = mp[numberpos[0]]
    if 0 < numberpos[1]:
        if is_symbol(row[left]):
            return True
    # row of number, right end
    if numberpos[2] < mapwidth:
        if is_symbol(row[right - 1]):
            return True
    if numberpos[0] < (mapheight - 1):
        row = mp[numberpos[0] + 1]
        for col in range(left, right):
            if is_symbol(row[col]):
                return True
    return False


def extract_number(mp: list[str], numberpos: tuple) -> int:
    """Extract the number specified by numberpos from the map mp.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.
    numberpos : tuple
        Tuple specifying number position in mp (row, start, stop).

    Returns
    -------
    int
        Number found at the specified position.
    """
    row = mp[numberpos[0]]
    return int(row[numberpos[1]:numberpos[2]])


def extract_part_numbers(mp: list[str], numberposs: set[tuple]) -> set[int]:
    """Extract all part numbers from the map.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.
    numberposs : set[tuple]
        Set of number position tuples (row, start, stop).

    Returns
    -------
    set[int]
        Set of part numbers.
    """
    return [
        extract_number(mp, numberpos)
        for numberpos in numberposs
        if check_adjacent(mp, numberpos)]


def extract_point_numberposs(
    row: str
    , ctr_coord: tuple[str]
) -> list[tuple[int]]:
    """Extract number coordinates adjacent to a coordinate on a row.

    If the specified coordinate has a digit, then there can only be
    one number. If not, then there could be one number on the left
    and/or one number on the right of the specified column position.

    Parameters
    ----------
    row : str
        The map row corresponding to row ctr_coord[0].
    ctr_coord : tuple[str]
        Tuple of two integers (row, col) indicating the coordinate with
        two adjacent cells.        

    Returns
    -------
    list[tuple[int]]
        List containing zero, one or two number positions.
    """
    if row[ctr_coord[1]].isdigit():
        return [get_numberpos_mid(row, ctr_coord)]
    result = []
    rw = ctr_coord[0]
    cl = ctr_coord[1] - 1
    if row[cl].isdigit():
        result += [get_numberpos_left(row, (rw, cl))]
    cl = ctr_coord[1] + 1
    if row[cl].isdigit():
        result += [get_numberpos_right(row, (rw, cl))]
    return result


def extract_coordadjacent_numberposs(
    mp: list[str]
    , start_coord: tuple[int]
) -> list[tuple[int]]:
    """Extract number positions adjacent to a specified coordinate.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.
        
    start_coord : tuple[int]
        Tuple of two integers (row, col) indicating the coordinate with
        eight adjacent cells.

    Returns
    -------
    list[tuple[int]]
        List of number coordinate tuples that are adjacent to the specified
        coordinate.
    """
    rw0 = start_coord[0]
    # check the line above
    rw = start_coord[0] - 1
    r1 = extract_point_numberposs(
        mp[rw]
        , (rw, start_coord[1]))
    # check on the line, left side
    cl = start_coord[1] - 1
    if mp[rw0][cl].isdigit():
        r2a = [get_numberpos_left(mp[rw0], (rw0, cl))]
    else:
        r2a = []
    # check on the line, right side
    cl = start_coord[1] + 1
    if mp[rw0][cl].isdigit():
        r2b = [get_numberpos_right(mp[rw0], (rw0, cl))]
    else:
        r2b = []
    rw = start_coord[0] + 1
    # check on the line below
    r3 = extract_point_numberposs(
        mp[rw]
        , (rw, start_coord[1]))
    return r1 + r2a + r2b + r3


def extract_gears_numposs(
    mp: list[str]
) -> dict[tuple[int], list[tuple[int]]]:
    """Extract dictionary of adjacent number positions.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.

    Returns
    -------
    dict[tuple[int], list[tuple[int]]]
        Dictionary of gear ratios, keyed by coordinates of asterisks.
    """
    return {
        (rowidx, colidx): v
        for rowidx, row in enumerate(mp)
        for colidx, ch in enumerate(row)
        if '*' == ch and 2 == len(
            v := extract_coordadjacent_numberposs(mp, (rowidx, colidx)))}

def calc_gear_ratio(mp: list[str], gr_list: list[tuple]) -> int:
    """Calculate the gear ratio given the map and list of adjacent number positions.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.
    gr_list : list[tuple]
        List of number coordinate triplets (row, start, stop).
        Must have exactly two elements.

    Returns
    -------
    int
        Product of the two numbers identified by gr_list.
    """
    nums = [
        extract_number(mp, npos)
        for npos in gr_list]
    return nums[0] * nums[1]


def calc_gear_ratios(mp: list[str]) -> dict[tuple[int], int]:
    """Compute a dictionary of gear ratios keyed by asterisk coordinates.

    Parameters
    ----------
    mp : list[str]
        Map as a list of strings representing rows.

    Returns
    -------
    dict[tuple[int], int]
        Dictionary of gear ratios, keyed by coordinates of asterisks.
        
    """
    return {
        k: calc_gear_ratio(mp, v)
        for k, v in extract_gears_numposs(mp).items()}


def calc_gear_ratios_sum(gear_ratio_dict: dict[tuple[int], int]) -> int:
    """Sum up dict of gear ratios.

    Parameters
    ----------
    gear_ratio_dict : dict[tuple[int], int]
        Dictionary of gear ratios, keyed by coordinates of asterisks.

    Returns
    -------
    int
        Sum of all gear ratios in the dictionary.
    """
    return sum([
        v
        for k, v in gear_ratio_dict.items()])

# day04.py
"""Computation for 2023 day 3"""


def parse_numberset(s: str) -> list[int]:
    """Parse a set of space-separated numbers.

    May be multiple consecutive spaces for one delimiter.

    Parameters
    ----------
    s : str
        _description_

    Returns
    -------
    list[int]
        Numberset.
    """
    ss = s.strip()
    return [
        int(sss)
        for sss in ss.split()]


def parse_numberset_pair(s: str) -> list:
    """Parse a winning and obtained pair of number sets.

    Parameters
    ----------
    s : str
        Number sets are separated by '|'.

    Returns
    -------
    list
        Numberset_pair, List of two items:
            [0]: winning numbers, list[int], no dupes?
            [1]: numbers obtained, list[int], no dupes?
    """
    return [
        parse_numberset(ss)
        for ss in s.split('|')]


def parse_card(line: str) -> tuple:
    """Parse a card encoded on in a single string.

    Parameters
    ----------
    line : str
        Line of text containin a card.

    Returns
    -------
    tuple
        Tuple of two items:
        [0]: card number, int
        [1]: numberset_pair, List of two items:
            [0]: winning numbers, list[int], no dupes?
            [1]: numbers obtained, list[int], no dupes?
    """
    parts = line.split(':')
    return (
        int(parts[0][5:])
        , parse_numberset_pair(parts[1]))


def parse_cards(lines: list[str]) -> list:
    """Parse a list of strings, each string is a card.

    Parameters
    ----------
    lines : list[str]
        List of strings, each one is a card.

    Returns
    -------
    list
        List of cards from parse_card.
    """
    return [
        parse_card(line)
        for line in lines]


def count_card_matches(card: tuple[list[int]]) -> int:
    """Count number of matches for a card.

    Parameters
    ----------
    card : tuple[list[int]]
        Tuple of two items:
        [0]: card number, int
        [1]: numberset_pair, List of two items:
            [0]: winning numbers, list[int], no dupes?
            [1]: numbers obtained, list[int], no dupes?

    Returns
    -------
    int
        Number of values in the winning and obtained values
        that are equal.
    """
    # if numbers allow duplicates?
    # wins = nsp[1][0].copy()
    # haves = nsp[1][1].copy()
    # intersection = []
    # for w in wins:
    #     if w in haves:
    #         intersection.append(w)
    #         haves.remove(w)
    # return len(intersection)
    wins = set(card[1][0])
    haves = set(card[1][1])
    return len(wins & haves)


def convert_matches_to_points(m: int) -> int:
    """Calculate points for a given number of matches for part a.

    Parameters
    ----------
    m : int
        Number of matches for some card.

    Returns
    -------
    int
        Number of points corresponding to m.
    """
    if 0 == m:
        return 0
    elif 1 == m:
        return 1
    return 2 ** (m - 1)


def calc_points(cards: list) -> int:
    """Calculate a list of points corresponding to a list of cards.

    Parameters
    ----------
    cards : list
        List of cards as from parse_cards.

    Returns
    -------
    int
        List of integer number of points per card.
    """
    return sum([
        convert_matches_to_points(count_card_matches(card))
        for card in cards])

def count_matches(cards: list) -> list[int]:
    """Obtain a list of matches, one for each card.

    Parameters
    ----------
    cards : list
        List of cards as from parse_cards.

    Returns
    -------
    list[int]
        List of numbers of matches corresponding to each card.
    """
    return [
        count_card_matches(card)
        for card in cards]


def count_copies(mcs: list[int]) -> list[int]:
    """Count copies of cards based on matches.

    Parameters
    ----------
    mcs : list[int]
        List of matches, one per card, as per count_matches function.

    Returns
    -------
    list[int]
        List of number of copies of each card (positionally).
    """
    result = [1 for mc in mcs]
    for i, mc in enumerate(mcs):
        if 0 < mc:
            for j in range(i + 1, i + mc + 1):
                result[j] += result[i]
    return result

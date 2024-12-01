# day02.py

opponent_code = {
    'A': 'Rock'
    , 'B': 'Paper'
    , 'C': 'Scissors'}
self_code = {
    'X': 'Rock'
    , 'Y': 'Paper'
    , 'Z': 'Scissors'}
self_code_b = {
    'X': -1
    , 'Y': 0
    , 'Z': 1}
rps_order = ['Rock', 'Paper', 'Scissors']


def decode_opponent(code):
    return opponent_code[code]


def decode_self(code):
    return self_code[code]

def decode_self_b(code):
    return self_code_b[code]


def read_rps_strategy(fname) -> list:
    """Sets up a generator of encrypted strategy tuples.

    Retrieves space-delimited encoded strategy pairs
    like `('A', 'Y')`).

    Parameters
    ----------
    fname : str or pathlib.Path
        Path to file to read.

    Returns
    -------
    generator
        Yields 2-tuples of encoded opponent and self
        strategy codes.
    """
    with open(fname, 'r', encoding='UTF-8') as inp:
        lns = inp.read().splitlines()
    return (tuple(v.split(' ')) for v in lns)


def gen_rps_results(rps_strategy):
    """Creates a generator of trial scores.

    Parameters
    ----------
    rps_strategy : generator
        Generator of tuples of opponent actions
        and self actions.

    Yields
    -------
    generator
        Scored outcomes generator.
    """
    rps_dict = build_rps_dict(rps_order)
    rps_to_int = {
        o: i
        for i, o in enumerate(rps_order)}
    return (
        rps_to_int[decode_self(self)]
        + 1
        + 3 * (
            1
            + rps_dict[(
                decode_opponent(opp)
                , decode_self(self))])
        for opp, self in rps_strategy)


def gen_rps_results_b(rps_strategy):
    rps_dict = build_rps_dict(rps_order)
    rps_to_int = {
        o: i
        for i, o in enumerate(rps_order)}
    return (
        rps_to_int[decode_self(self)]
        + 1
        + 3 * (
            1
            + rps_dict[(
                decode_opponent(opp)
                , decode_self(self))]
            )
        for opp, self in rps_strategy)


def cmp(i: int, j: int, n: int) -> int:
    """Generate lookup for tuples of integer plays.

    The returned result is equivalent to a matrix of outcomes.

    The algorithm follows the 

    Parameters
    ----------
    i : int
        Play by opponent, as index of rps_order
    j : int
        Play by self, as index of rps_order
    n : int
        Number of entries in rps_order

    Returns
    -------
    int
        -1 means self lost, 1 means self won, and 0 means tie.
    """
    result = 0
    if i == j:
        pass
    else:
        d = j - i
        if d < 0:  # stripes parallel to main diagonal
            mul = 1
        else:
            mul = -1
        v = d % 2
        result = mul * (2 * v - 1)
    return result


def build_rps_dict(order_list):
    """Build rps dictionary.

    The returned dictionary can be used to look up
    the outcome of a trial (1=win, -1=loss, 0=tie).

    Parameters
    ----------
    order_list : list
        List of strings indicating the order of wins.
        E.g. for ['Rock', 'Paper', 'Scissors'], 'Rock'
        beats 'Scissors', 'Paper' beats 'Rock', and 'Scissors'
        beats 'Paper'.

    Returns
    -------
    dict
        Keyed by all possible 2-tuples of opponent play (e.g. 'Rock')
        and self play (e.g. 'Paper'). Used for scoring trials.
        Values indicate outcome as -1=self loses, 0=tie, and
        1=self wins.
    """
    rps_to_int = {
        o: i
        for i, o in enumerate(order_list)}
    return {
        (opp, self): -cmp(
            rps_to_int[opp]
            , rps_to_int[self]
            , len(order_list) - 1)
        for opp in order_list
        for self in order_list}

def build_rps_dict_b(order_list):
    rps_to_int = {
        o: i
        for i, o in enumerate(order_list)}
    return {
        (opp, self): -cmp(
            rps_to_int[opp]
            , rps_to_int[self]
            , len(order_list) - 1)
        for opp in order_list
        for self in order_list}


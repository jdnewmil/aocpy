# day01.py

import heapq

def split_list(slist: list) -> list:
    last_i = 0
    for i, v in enumerate(slist):
        if '' == v:
            if last_i < i:
                yield slist[last_i:i]
            last_i = i+1
    if last_i < len(slist):
        yield slist[last_i:len(slist)]
    return StopIteration


def read_elf_loads(fname) -> list:
    with open(fname, 'r', encoding='UTF-8') as inp:
        lns = inp.read().splitlines()
    return ([float(v) for v in l] for l in split_list(lns))


def find_max_load(elf_loads):
    max_i = None
    max_load = -1.
    for i, ld in enumerate(elf_loads):
        load = sum(ld)
        if max_load < load:
            max_load = load
            max_i = i
    if -1.0 == max_load:
        max_load = None
    return max_i, max_load


def gen_elf_sums(elf_loads):
    return (
        (sum(l), i)
        for i, l in enumerate(elf_loads))

def find_max_load3(elf_loads):
    sum_iter = gen_elf_sums(elf_loads)
    heap = [next(sum_iter) for i in range(3)]
    heapq.heapify(heap)
    for t in sum_iter:
        heapq.heappushpop(heap, t)
    return sorted(heap, reverse=True)

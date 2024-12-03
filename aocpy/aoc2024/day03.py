"""AOC 2024 Day03 functions."""

from typing import Optional, TypeAlias
from dataclasses import dataclass
import re

# CPU2: TypeAlias = 

@dataclass
class Op2:
    op: str
    arg1: int
    arg2: int

    @property
    def value(self) -> int:
        assert 'mul' == self.op
        return self.arg1 * self.arg2
    
    def exec(self, cpu: 'CPU2'):
        cpu.result = None
        if 'mul' == self.op and CPU2.RUN == cpu.state:
            cpu.result = self.arg1 * self.arg2
        elif 'do' == self.op:
            cpu.state = CPU2.RUN
        elif "don't" == self.op:
            cpu.state = CPU2.SKIP


def op_pat(op_list: list[str]) -> str:
    dpat = '\d{1,3}'
    pat_op0 = '|'.join(op_list)
    return f'({pat_op0})\((({dpat}), *({dpat}))?\)'
    

class Op_Parse_Iter:
    def __init__(self, init_str: str, op_list: list[str]):
        self.init_str = init_str
        self.src = None
        self.op_list = op_list
        self.pat = None

    def __iter__(self):
        self.src = self.init_str
        pat_op = op_pat(self.op_list)
        pat = f'(.*?){pat_op}(.*)'
        self.pat = re.compile(pat)
        return self
    

    def __next__(self):
        match = self.pat.match(self.src)
        if not match:
            raise StopIteration
        if 'mul' == match.group(2):
            op = Op2(match.group(2), int(match.group(4)), int(match.group(5)))
        elif match.group(2) in ['do', "don't"]:
            op = Op2(match.group(2), 0, 0)
        else:
            raise ValueError(f'unknown op {match.group(2)}')
        self.src = match.group(6)
        return match.group(1), op, match.group(5)


class CPU2:
    RUN = 1
    SKIP = 2
    def __init__(self):
        self.state = CPU2.RUN
        self.result = None

    def run(self, op_list: list[Op2]) -> list[int]:
        result = []
        for op in op_list:
            op.exec(self)
            if self.result is not None:
                result.append(self.result)
        return result


# (.*?)(mul)\((\d{1,3}),(\d{1,3})\)(.*)

def get_values_day03a(ln: str) -> list[int]:
    return [
        op.value
        for pre, op, post in Op_Parse_Iter(ln, ['mul'])]

def get_ops_day03a(ln: str, op_list: list[str]) -> list[Op2]:
    return [
        op
        for pre, op, post in Op_Parse_Iter(ln, op_list)]

def calc_day03b(op_list: list[Op2]) -> int:
    cpu = CPU2()
    return sum(cpu.run(op_list=op_list))

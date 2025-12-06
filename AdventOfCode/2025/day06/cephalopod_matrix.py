""" Cephalopod math objects """
from enum import Enum
from typing import List, Tuple, Union

class Operator(Enum):
    """ Operator for a cephalopod matrix"""
    ADD = '+'
    MULTIPLY = '*'

class Column:
    """ Column of a cephalopod matrix"""
    cells: List[int]
    operator: Operator

    def __init__(self, raw_list: Tuple[Union[str, int]]):
        self.operator = Operator(raw_list[-1])
        self.cells = [int(cell) for cell in raw_list[:-1]]

    def solve(self) -> int:
        """ Solve the column"""
        if self.operator == Operator.ADD:
            return sum(self.cells)
        if self.operator == Operator.MULTIPLY:
            result = 1
            for cell in self.cells:
                result *= cell
            return result

    def __repr__(self):
        return f'Column({self.cells}, {self.operator})'

class CephalopodMatrix:
    """ Cephalopod matrix"""
    columns: List[Column]

    def __init__(self, raw_matrix: List[List[Union[str, int]]]):
        self.columns = [Column(column) for column in raw_matrix]

    @classmethod
    def from_rows(self, rows: List[str]) -> 'CephalopodMatrix':
        """ Create a cephalopod matrix from a list of rows"""
        rows: List[List[str]] = [row.split() for row in rows]
        columns = list(zip(*rows))
        return CephalopodMatrix(columns)

    def solve(self) -> List[int]:
        """ Solve the matrix"""
        return [column.solve() for column in self.columns]

    def __repr__(self):
        return f'CephalopodMatrix({self.columns})'

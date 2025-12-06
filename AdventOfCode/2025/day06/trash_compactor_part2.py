""" Advent Of Code 2025: Day 05 Part 2 """
import sys
from typing import List

def solve_operation(operator: str, numbers: List[int]):
    """ Solve a single operation """
    subtotal = None
    if operator == '+':
        subtotal = sum(numbers)
    if operator == '*':
        subtotal = 1
        for number in numbers:
            subtotal *= number
    return subtotal

def solve(matrix: str) -> int:
    """ Solve the matrix """
    rows = matrix.splitlines()
    length = len(rows[0])
    numbers = []
    total = 0
    operator = None
    for i in range(length):
        column = [row[i] for row in rows]
        if all(c == ' ' for c in column):
            total += solve_operation(operator, numbers)
            numbers = []
            operator = None
            continue

        if not operator:
            operator = column[-1]
        
        joined_column = ''.join(column[:-1])
        while ' ' in joined_column:
            joined_column = joined_column.replace(' ', '')
        numbers.append(int(joined_column))
    else:
        total += solve_operation(operator, numbers)

    return total

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read()

    print(f'Grand total: {solve(data)}')

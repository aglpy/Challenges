""" Advent Of Code 2025: Day 05 Part 1 """
import sys
from cephalopod_matrix import CephalopodMatrix

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()
    
    cephalopod_matrix = CephalopodMatrix.from_rows(data.splitlines())

    print(cephalopod_matrix.columns[0].normalize_cells())

    print(f'Grand total: {sum(cephalopod_matrix.solve())}')

""" Advent Of Code 2025: Day 04 Part 1 """
import sys
from rolls_grid import RollsGrid

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()

    rolls_grid = RollsGrid(data)
    print(f'Pickable rolls: {rolls_grid.pickable_rolls}')

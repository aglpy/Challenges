""" Advent Of Code 2025: Day 04 Part 2 """
import sys
from rolls_grid import RollsGrid

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()

    rolls_grid = RollsGrid(data)
    print(f'Rolls picked: {len(rolls_grid.pick_rolls())}')

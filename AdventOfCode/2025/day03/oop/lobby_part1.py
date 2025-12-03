""" Advent of Code 2025, Day 03: Lobby Part 1 """
import sys
from bank import Bank

if __name__ == "__main__":
    input_filename = sys.argv[1]
    
    with open(input_filename, 'r', encoding="utf-8") as input_file:
        input_data = input_file.read().strip()
    
    banks = [Bank.from_string(batteries) for batteries in input_data.splitlines()]

    jolts = sum(bank.highest_jolts(2) for bank in banks)
    print(f'Highest jolts: {jolts}')

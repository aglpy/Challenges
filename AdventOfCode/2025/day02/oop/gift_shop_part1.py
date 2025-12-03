""" Advent of Code 2025, Day 02: Gift Shop """
import sys
from typing import List
from interval import Interval

def find_invalid_ids(intervals: List[Interval]) -> List[int]:
    """ Find the IDs of the gifts that are invalid """
    return [invalid_id for interval in intervals for invalid_id in interval.invalid_ids]

if __name__ == "__main__":
    input_filename = sys.argv[1]
    
    with open(input_filename, 'r', encoding="utf-8") as input_file:
        input_data = input_file.read().strip()
    
    intervals_str = input_data.split(",")
    intervals = [Interval.from_string(interval_str) for interval_str in intervals_str]

    invalid_ids = find_invalid_ids(intervals)
    print(f'Invalid id sum: {sum(invalid_ids)}')

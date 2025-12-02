""" Advent of Code 2025, Day 01: Secret Entrance """
import sys

turns = open(sys.argv[1]).readlines()

zero_counter = 0
position = 50
for turn in turns:
    if turn[0] == 'R':
        position += int(turn[1:])
    else:
        position -= int(turn[1:])
    position = position % 100
    if position == 0:
        zero_counter += 1

print(zero_counter)

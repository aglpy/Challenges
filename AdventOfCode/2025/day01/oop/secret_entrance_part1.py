""" Advent of Code 2025, Day 01: Secret Entrance """
import sys

from dial import Dial

def turn_dial(dial: Dial, turn_instructions: str):
    """ Turn the dial based on the turn instruction
    
    Arguments:
        turn (str): The turn instruction: XN where X can be L (left) or R (right) and N the number
                    of ticks to turn
    """
    direction = turn_instructions[0]
    ticks = int(turn_instructions[1:])
    if direction == "L":
        for _ in range(ticks):
            dial.turn_left()
    if direction == "R":
        for _ in range(ticks):
            dial.turn_right()

def guess_password(dial: Dial, turns_data: str) -> int:
    """ Guess the password
    
    Arguments:
        dial (Dial): The dial object
        turns_data (str): The turns data, a text with rows, each row must be a turn instructions: XN
                            where X can be L (left) or R (right) and N the number of ticks to turn
    
    Returns:
        int: The password
    """
    turns = [turn.strip() for turn in turns_data.splitlines()]
    zero_counter = 0
    for turn in turns:
        turn_dial(dial, turn)
        if dial.position == 0:
            zero_counter += 1
    return zero_counter

if __name__ == "__main__":
    input_filename = sys.argv[1]
    
    with open(input_filename, 'r', encoding="utf-8") as input_file:
        input_data = input_file.read().strip()
    
    default_dial = Dial(50)
    password = guess_password(default_dial, input_data)
    print(f"Password: {password}")

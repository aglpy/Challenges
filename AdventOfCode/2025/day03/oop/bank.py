""" Battery bank objects """
from dataclasses import dataclass
from typing import List

@dataclass(eq=False)
class Battery:
    """ Battery object """
    jolts: int

    def __add__(self, other: 'Battery') -> 'Battery':
        if not other:
            return self
        return Battery(int(f'{self.jolts}{other.jolts}'))
    
    def __radd__(self, other) -> 'Battery':
        return self.__add__(other)
    
    def __lt__(self, other: 'Battery') -> bool:
        return self.jolts < other.jolts

class Bank:
    """ Battery bank """

    def __init__(self, batteries: list[Battery]):
        self.batteries = batteries

    @classmethod
    def from_string(cls, batteries_str: str) -> 'Bank':
        """ Create a bank from a string """
        batteries = [Battery(int(jolt)) for jolt in batteries_str]
        return cls(batteries)

    def highest_jolts(self, pick_batteries: int) -> int:
        """ Calculate the jolts of the bank picking certain number of batteries """
        batteries: List[Battery] = []
        lower_index = 0
        higher_index = 1 - pick_batteries
        for _ in range(pick_batteries):
            battery = max(self.batteries[lower_index:higher_index])
            batteries.append(battery)
            lower_index = self.batteries.index(battery) + 1
            higher_index += 1
            if not higher_index:
                higher_index = len(self.batteries)
        return sum(batteries).jolts

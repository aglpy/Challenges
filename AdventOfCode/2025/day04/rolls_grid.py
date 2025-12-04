""" Rolls grid objects """
from dataclasses import dataclass
from typing import List, Literal, Optional

@dataclass
class Neighborhood:
    """ Neighborhood of a slot """
    nw: bool
    n: bool
    ne: bool
    w: bool
    e: bool
    sw: bool
    s: bool
    se: bool

    @property
    def neighboors(self) -> int:
        """ Returns the number of neighboors """
        return sum([self.nw, self.n, self.ne,
                    self.w, 0000000, self.e, 
                    self.sw, self.s, self.se])

class RollsGrid:
    """ Rolls grid """

    def __init__(self, grid: str):
        self.grid: List[List[str]] = [list(line) for line in grid.splitlines()]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def has_roll(self, top: int, left: int) -> bool:
        """ Checks if there is a roll at the given position """
        if not 0 <= top < self.height or not 0 <= left < self.width:
            return False
        return self.grid[top][left] == "@"

    def neighborhood(self, top: int, left: int) -> Neighborhood:
        """ Returns the neighborhood of the given position """
        return Neighborhood(
            nw=self.has_roll(top-1, left-1),
            n=self.has_roll(top-1, left),
            ne=self.has_roll(top-1, left+1),
            w=self.has_roll(top, left-1),
            e=self.has_roll(top, left+1),
            sw=self.has_roll(top+1, left-1),
            s=self.has_roll(top+1, left),
            se=self.has_roll(top+1, left+1)
        )

    def is_pickable(self, top: int, left: int) -> bool:
        """ Checks if the roll at the given position is pickable """
        if not self.has_roll(top, left):
            return False
        neighborhood = self.neighborhood(top, left)
        return neighborhood.neighboors < 4

    @property
    def pickable_rolls(self) -> int:
        """ Returns the number of pickable rolls """
        return sum(self.is_pickable(top, left)
                   for top in range(self.height)
                   for left in range(self.width))

    def pick_roll(self, top: int, left: int) -> Optional[Literal['@']]:
        """ Pick a roll if pickable """
        if self.is_pickable(top, left):
            roll = self.grid[top][left]
            self.grid[top][left] = "."
            return roll

    def pick_rolls(self) -> List[Literal['@']]:
        """ Picks the rolls """
        rolls = []
        while self.pickable_rolls:
            for top in range(self.height):
                for left in range(self.width):
                    roll = self.pick_roll(top, left)
                    if roll:
                        rolls.append(roll)
        return rolls

    def __repr__(self):
        return "\n".join(self.grid)

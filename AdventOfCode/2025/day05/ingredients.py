""" Ingredients objects """
from typing import Optional, Union

class IngredientRange:
    """ Range of fresh ingredients """
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    @classmethod
    def from_str(cls, string: str):
        start, end = string.split('-')
        return cls(int(start), int(end))

    @property
    def total_ingredients(self) -> int:
        return self.end - self.start + 1

    def __contains__(self, item: Union[int, str]):
        if isinstance(item, str):
            item = int(item)
        return self.start <= item <= self.end

    def __lt__(self, other: 'IngredientRange'):
        return self.start < other.start

    def __add__(self, other: 'IngredientRange') -> Optional['IngredientRange']:
        if self.start <= other.start and self.end >= other.start - 1:
            return IngredientRange(self.start, max(self.end, other.end))
        if other.start <= self.start and other.end >= self.start - 1:
            return IngredientRange(other.start, max(self.end, other.end))
        return None
    
    def __repr__(self):
        return f'IngredientRange({self.start}, {self.end})'

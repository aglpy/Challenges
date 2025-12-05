""" Advent Of Code 2025: Day 05 Part 2 """
import sys
from typing import List, Optional
from ingredients import IngredientRange

def total_fresh_ingredients(fresh_ingredients: List[str]) -> int:
    """ Check how many fresh ingredients are in total """
    fresh_ingredients = [IngredientRange.from_str(ingredient_range) 
                         for ingredient_range in fresh_ingredients]
    fresh_ingredients.sort()

    fresh_ingredient_count = 0
    temporary_joined_range: IngredientRange = fresh_ingredients.pop(0)
    for ingredient_range in fresh_ingredients:
        new_range = temporary_joined_range + ingredient_range
        if new_range:
            temporary_joined_range = new_range
        else:
            fresh_ingredient_count += temporary_joined_range.total_ingredients
            temporary_joined_range = ingredient_range
    else:
        fresh_ingredient_count += temporary_joined_range.total_ingredients

    return fresh_ingredient_count

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()
    fresh_ingredients_ranges, _ = data.split('\n\n')
    fresh_ingredients_ranges = fresh_ingredients_ranges.strip().split('\n')

    fresh_ingredients = total_fresh_ingredients(fresh_ingredients_ranges)
    print(f'Total fresh ingredients: {fresh_ingredients}')

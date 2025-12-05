""" Advent Of Code 2025: Day 05 Part 1 """
import sys
from typing import List
from ingredients import IngredientRange

def check_fresh_ingredients(fresh_ingredients: List[str], all_ingredients: List[str]) -> int:
    """ Check how many fresh ingredients are in the all ingredients list """
    fresh_ingredients = [IngredientRange.from_str(ingredient_range) 
                         for ingredient_range in fresh_ingredients]
    fresh_ingredient_count = 0
    for ingredient in all_ingredients:
        for ingredient_range in fresh_ingredients:
            if ingredient in ingredient_range:
                fresh_ingredient_count += 1
                break
    return fresh_ingredient_count

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()
    fresh_ingredients_ranges, all_ingredients = data.split('\n\n')
    fresh_ingredients_ranges = fresh_ingredients_ranges.strip().split('\n')
    all_ingredients = all_ingredients.strip().split('\n')

    fresh_ingredients = check_fresh_ingredients(fresh_ingredients_ranges, all_ingredients)
    print(f'Fresh ingredients: {fresh_ingredients}')

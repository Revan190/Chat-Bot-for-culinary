def search_by_ingredients(ingredients, recipes):
    matching_recipes = []
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def filter_recipes_by_type_and_diet(recipes, dish_type=None, diet=None):
    filtered_recipes = recipes
    if dish_type:
        filtered_recipes = [r for r in filtered_recipes if r['type'] == dish_type]
    if diet:
        filtered_recipes = [r for r in filtered_recipes if diet in r['dietary_restrictions']]
    return filtered_recipes

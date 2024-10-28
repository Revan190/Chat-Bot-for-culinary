import json
import logging

def save_recipe(recipe):
    try:
        recipes = []
        try:
            with open('data.json', 'r') as f:
                recipes = json.load(f)
        except json.JSONDecodeError:
            pass

        recipes.append(recipe)
        with open('data.json', 'w') as f:
            json.dump(recipes, f, indent=4)

        logging.info("Recipe successfully saved!")
        print("Recipe successfully saved!")
    except Exception as e:
        logging.error(f"Error when saving recipe: {e}")

def save_favorite_recipe(recipe, user_id):
    try:
        with open(f'{user_id}_favorites.json', 'a') as f:
            json.dump(recipe, f)
            f.write("\n")
        logging.info("Favorite recipe successfully saved!")
    except Exception as e:
        logging.error(f"Error when saving favorite recipe: {e}")

def filter_and_sort_recipes(recipes, sort_by=None, max_time=None, max_calories=None):
    if max_time is not None:
        recipes = [r for r in recipes if r.get('time', float('inf')) <= max_time]
    if max_calories is not None:
        recipes = [r for r in recipes if r.get('calories', float('inf')) <= max_calories]
    
    if sort_by == "time":
        return sorted(recipes, key=lambda x: x['time'])
    
    return recipes

def get_recipes(ingredients):
    if not ingredients:
        logging.warning("No ingredients provided to get_recipes.")
        return []

    try:
        with open('data.json', 'r') as f:
            recipes = json.load(f)
        
        matching_recipes = []
        for recipe in recipes:
            if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
                matching_recipes.append(recipe)

        return matching_recipes
    except Exception as e:
        logging.error(f"Error loading recipes: {e}")
        return []

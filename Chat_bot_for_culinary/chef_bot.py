import json
import logging
import random
from recipes.recipe_manager import get_recipes, save_recipe

class ChefBot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.recipes_data_file = 'data.json'

    def handle_message(self, message):
        if message.startswith("/get_recipes"):
            ingredients = message[len("/get_recipes "):].split(",")
            return self.get_recipes(ingredients)
        elif message.startswith("/save_recipe"):
            recipe = self.parse_recipe(message[len("/save_recipe "):])
            self.save_recipe(recipe)
            return "Recipe saved!"
        elif message == "/cooking_tips":
            return self.cooking_tips()
        else:
            return "Unknown command."

    def get_recipes(self, ingredients):
        recipes = get_recipes(ingredients)
        if recipes:
            return json.dumps(recipes, indent=4)
        else:
            return "No matching recipes found."

    def save_recipe(self, recipe):
        save_recipe(recipe)

    def parse_recipe(self, recipe_str):
        parts = recipe_str.split(",")
        recipe = {}
        for part in parts:
            key, value = part.split(":")
            if key == "ingredients":
                recipe[key] = value.split(";")
            else:
                recipe[key] = value
        return recipe

    def cooking_tips(self):
        tips = [
            "Always taste your food as you cook.",
            "Let meat rest after cooking for juicier results.",
            "Use fresh herbs for better flavor.",
            "Don't overcrowd the pan when sautéing.",
            "Use a thermometer to check meat doneness."
        ]
        return random.choice(tips)

def chef_bot_response(message):
    bot = ChefBot()
    return bot.handle_message(message)

def cooking_tips():
    bot = ChefBot()
    return bot.cooking_tips()

if __name__ == "__main__":
    bot = ChefBot()
    while True:
        user_input = input("Enter command: ")
        response = bot.handle_message(user_input)
        print(response)

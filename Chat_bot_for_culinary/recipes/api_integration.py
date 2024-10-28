import requests
import logging

cache = {}

def get_nutrition_info(ingredient):
    if ingredient in cache:
        logging.info(f"Using cached data for {ingredient}.")
        return cache[ingredient]
    
    try:
        logging.info(f"Fetching nutritional information for {ingredient}.")
        response = requests.get(f"https://api.nutritionix.com/v1_1/search/{ingredient}?results=0:1&fields=*&appId=YOUR_APP_ID&appKey=YOUR_APP_KEY")
        response.raise_for_status()
        data = response.json()
        cache[ingredient] = data
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting nutritional information: {e}")
        return None

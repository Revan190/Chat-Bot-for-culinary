import logging
import nltk
from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from recipes.recipe_manager import get_recipes, save_recipe, save_favorite_recipe
from recipes.search import search_by_ingredients, filter_recipes_by_type_and_diet
from utils.logging import log_user_request
from utils.input_validation import get_user_input
from chef_bot import chef_bot_response, cooking_tips

nltk.download('punkt')
nltk.download('stopwords')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/search', methods=['POST'])
def search():
    logging.info("Received search request.")
    ingredients = request.form.get('ingredients').split(',')
    dish_type = request.form.get('dish_type')
    diet = request.form.get('diet')

    log_user_request(user_id='anonymous', request=f'Search with ingredients: {ingredients}, type: {dish_type}, diet: {diet}')
    logging.info(f"User  input - Ingredients: {ingredients}, Dish Type: {dish_type}, Diet: {diet}")

    try:
        ingredients = [word for word in word_tokenize(' '.join(ingredients)) if word.lower() not in stopwords.words('english')]
        logging.info("Ingredients processed successfully.")
    except Exception as e:
        logging.error(f"Error processing ingredients: {e}")
        return render_template('error.html', message="An error occurred while processing your request.")

    recipes = get_recipes(ingredients)
    results = search_by_ingredients(ingredients, recipes)
    results = filter_recipes_by_type_and_diet(results, dish_type, diet)

    logging.info(f"Found {len(results)} recipes.")
    return render_template('results.html', recipes=results)

@app.route('/ask_chef', methods=['POST'])
def ask_chef():
    question = request.form.get('question')
    answer = chef_bot_response(question)
    return render_template('menu.html', answer=answer)

@app.route('/cooking_tips')
def cooking_tips_route():
    tips = cooking_tips()
    return render_template('menu.html', tips=tips)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

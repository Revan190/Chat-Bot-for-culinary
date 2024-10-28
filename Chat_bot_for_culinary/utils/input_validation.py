def get_user_input():
    while True:
        user_input = input("Enter the ingredients separated by commas: ").strip()
        if user_input:
            ingredients = [ingredient.strip() for ingredient in user_input.split(',')]
            return ingredients
        else:
            print("Error: Input cannot be empty. Please try again.")

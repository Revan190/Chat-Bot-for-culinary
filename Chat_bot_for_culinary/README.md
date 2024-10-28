
---
## Project Structure

```
culinary_chatbot/                # Main project directory
│
├── app.py                        # Main file of the application that runs the Flask server
├── chatbot.ipynb                # Jupyter Notebook for interactive experimentation and prototyping
├── chef_bot.py                   # Logic for the chef bot that handles user queries and responses
├── data.json                     # JSON file containing recipe data
│
├── recipes/                      # Directory containing recipe-related functionalities
│   ├── __init__.py               # Initialization file for the recipes package
│   ├── recipe_manager.py         # Functions for managing recipes (saving, retrieving)
│   ├── search.py                 # Functions for searching recipes based on ingredients and filters
│   └── api_integration.py        # Functions for integrating with external APIs (if applicable)
│
├── utils/                        # Directory for utility functions
│   ├── __init__.py               # Initialization file for the utils package
│   ├── input_validation.py        # Functions for validating user input
│   └── logging.py                # Functions for logging user requests and application events
│
├── templates/                    # Directory containing HTML templates for rendering
│   ├── __init__.py               # Initialization file for the templates package
│   ├── menu.html                 # HTML template for the main menu
│   └── results.html              # HTML template for displaying search results
│
├── requirements.txt              # File listing the required Python packages for the project
└── README.md                     # Project overview and instructions
```

## How to Run

1. **Create a Virtual Environment**: 
   Open your terminal and navigate to the project directory. Run the following command:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**:
   Install the necessary Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Launch the application by executing:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://localhost:5000`.

## How to Use

1. **Home Menu**: 
   When you open the application, you will see the main menu. You can enter ingredients, select a dish type, and specify dietary restrictions.

2. **Searching for Recipes**: 
   After entering your criteria, the chatbot will process your request and display relevant recipes based on the ingredients and filters provided.

3. **Asking the Chef**: 
   You can ask the chef bot for cooking tips or specific questions related to cooking, and it will provide responses based on its programmed logic.

4. **Cooking Tips**: 
   Access various cooking tips through the designated route in the menu.

## Future Enhancements

In the future, the chatbot may include:
- Integration with external recipe APIs for a more extensive recipe database.
- User authentication and personalized recipe recommendations.
- A mobile-friendly interface for easier access on smartphones and tablets.
- Enhanced user interaction features, such as voice commands and feedback.

Now... enjoy your first (or continue) cooking with your culinary chatbot!

--- 

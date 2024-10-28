import logging

logging.basicConfig(filename='chatbot.log', level=logging.INFO)

def log_user_request(user_id, request):
    logging.info(f'User  {user_id} requested: {request}')

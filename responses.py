
def handle_response(message) -> str:
    p_message = message.content.lower()
    
    if p_message == 'die':
        if str(message.author) == 'cletor':
            return -1
        else:
            return 'no you'
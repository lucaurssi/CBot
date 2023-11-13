
import random

def handle_response(message) -> str:
    p_message = message.content.lower()
    
    match p_message:
        case 'hello':
            return 'Hey there!'
       
        case 'roll':
            return 'rolling 1d6:   ' + str(random.randint(1, 6))
        
        case 'die':
            if str(message.author) == 'cletor':
                return -1
            else:
                return 'no you'
        case 'help':
            return "```\nCurrent commands:\n - hello\n - roll\n - help```"   


        case _:
            return ''
    
    
    

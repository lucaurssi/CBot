import bot
import storage

if __name__ == '__main__':
    TOKEN = storage.token_magic()
    
    bot.run_discord_bot(TOKEN)
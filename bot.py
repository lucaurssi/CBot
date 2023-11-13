
import discord
import responses

intents = discord.Intents.default()
intents.message_content = True

def token_magic():
    
    try:
        f = open("token.clt", "r")
        token = f.read()
        f.close()
        return token 
    except:
        token = input(f' please insert your discord token: ')
        f = open("token.clt", "w")
        f.write(token)
        f.close()
        return token

async def send_message(message, response):
    try:
        await message.channel.send(response)
    except Exception as e:
        print (e)


def run_discord_bot():
    TOKEN = token_magic()
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        print(f"{message.author} said: '{message.content}' in channel: '{message.channel}'")
        response = responses.handle_response(message)
        
        if response == -1:
            await send_message(message, 'Shutting down...')
            await client.close()
            return
        
        if response != '':
            await send_message(message, response)


    client.run(TOKEN)
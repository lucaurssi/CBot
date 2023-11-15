
import discord
from discord import app_commands
from discord.ext import commands
import random

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



def run_discord_bot():
    TOKEN = token_magic()
    bot = commands.Bot(command_prefix="!", intents = intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
    
    
    
    @bot.tree.command(name="hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"hey there, {interaction.user.display_name}!")
        
    
    
    @bot.tree.command(name="die")
    async def hello(interaction: discord.Interaction):
        if str(interaction.user.name) == 'cletor':
            await interaction.response.send_message(f"Shutting down...")
            await bot.close()
        else:
            print(f"Reporting: user '{interaction.user.name}' tryed to kill bot.")
            await interaction.response.send_message(f"Reporting user '{interaction.user.display_name}' for attempting murder.")



    # dice command 1d6 4d10 ... ndn
    @bot.tree.command(name="roll")
    @app_commands.describe(num__of_dice = "number of dice", size="size of the dice")
    async def roll(interaction: discord.Interaction, num__of_dice: int, size: int):
        if (num__of_dice <= 0 or size <= 0):
            await interaction.response.send_message(f"Dice values must be above zero")
            return
        if (num__of_dice >100 or size > 10000):
            await interaction.response.send_message(f"You can't possibly actually need that amount.")
            
        results = []
        for i in range(num__of_dice):
            result = random.randint(1, size)
            results.append(result)
        result = 0
        for i in results:
            result = result + i
        await interaction.response.send_message(f"you roll {num__of_dice}d{size}:   `{result}`   `{results}`")

    
    bot.run(TOKEN)
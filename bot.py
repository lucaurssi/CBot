
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

'''
    TO DO list:
    - embed GUI
    - improve documentation on !help
    - more commands
'''

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


def run_discord_bot(TOKEN):
    bot = commands.Bot(command_prefix="!", intents = intents)

    # ---------------------------------------------------------

    # !hello
    @bot.command(brief='Greets user.')
    async def hello(ctx): # ctx --> context
        print(f'[{ctx.author.name}] used /hello')
        await ctx.send(f"hey there, {ctx.author.mention}!")
        
    
    # ---------------------------------------------------------
    
    # !die
    @bot.command(brief='Shutdown bot if user has the permission.')
    async def die(ctx):
        if str(ctx.author.name) == 'cletor':
            await ctx.send(f"Shutting down...")
            await bot.close()
        else:
            print(f"Reporting: user '{ctx.author.name}' tryed to kill bot.")
            await ctx.send(f"Reporting user '{ctx.author.name}' for attempting murder.")

    # ---------------------------------------------------------

    # !roll
    @bot.command(brief='Usage: !roll num__of_dice size ')
    async def roll(ctx, num__of_dice, size):
        print(f'[{ctx.author.name}] used /roll {num__of_dice}d{size}')
        
        try:
            num__of_dice = int(num__of_dice)
            size = int(size)
        except:
            await ctx.send(f"Dice value must be a number '{num__of_dice}' '{size}'")
            return
        if (num__of_dice <= 0 or size <= 0):
            await ctx.send(f"Dice values must be above zero")
            return
        if (num__of_dice >100 or size > 10000):
            await ctx.send(f"You can't possibly actually need that amount.")
            return
            
        results = []
        for i in range(num__of_dice):
            result = random.randint(1, size)
            results.append(result)
        result = 0
        for i in results:
            result = result + i
        await ctx.send(f"you roll {num__of_dice}d{size}:   `{result}`   `{results}`")

    # --------------------------------------------------------
    
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!') # print on terminal
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)") 
            
            for command in bot.commands:
                print(f"- {command.name}")
                
        except Exception as e:
            print(e)
    
    bot.run(TOKEN)
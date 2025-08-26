
import discord
from discord.ext import commands
import random

import storage

intents = discord.Intents.default()
intents.message_content = True
privilege_list = []
'''
    TO DO list:
    - more commands
    - send log to log file
'''

def run_discord_bot(TOKEN):
    bot = commands.Bot(command_prefix="!", intents = intents)
    bot.remove_command('help')
    
    # ---------------------------------------------------------
    
    @bot.command()
    async def help(ctx, args=None):
        help_embed = discord.Embed(title="!help")
        command_names_list = [x.name for x in bot.commands]
        print(f'[{ctx.author.name}] used !help')

        # If there are no arguments, just list the commands:
        if not args:
            help_embed.add_field(
                name="List of supported commands:",
                value="\n".join("- "+x.name for x in bot.commands),
                inline=False
            )
            help_embed.add_field(
                name="Details",
                value="Type `!help <command name>` for more details about each command.",
                inline=False
            )

        # If the argument is a command, get the help text from that command:
        elif args in command_names_list:
            help_embed.add_field(
                name=args,
                value=bot.get_command(args).description
            )

        # If someone is just trolling:
        else:
            help_embed.add_field(
                name="Nope.",
                value="Don't think I got that command, boss!"
            )

        await ctx.send(embed=help_embed)
    
    # ---------------------------------------------------------

    # !hello
    @bot.command(description='Greets user.')
    async def hello(ctx): # ctx --> context
        print(f'[{ctx.author.name}] used !hello')
        await ctx.send(f"hey there, {ctx.author.mention}!")
        
    
    # ---------------------------------------------------------
    
    # !die
    @bot.command(description='Shutdown bot if user has the permission.')
    async def die(ctx):
        if ctx.author.name in privilege_list:
            await ctx.send(f"Shutting down...")
            await bot.close()
        else:
            print(f"Reporting: user '{ctx.author.name}' tryed to kill bot.")
            await ctx.send(f"Reporting user '{ctx.author.name}' for attempting murder.")

    # ---------------------------------------------------------

    # !roll
    @bot.command(description="Usage: ' !roll XdY ', where X and Y are numbers.")
    async def roll(ctx, dice):
        
        print(f'[{ctx.author.name}] used !roll {dice}')
        
        try:
            num__of_dice, size = dice.split('d')
            num__of_dice = int(num__of_dice)
            size = int(size)
        except:
            await ctx.send(f"Dice values must be numbers and must be separated by a ' d ' ( i.e.: !roll 1d6 )")
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
    
    # !admin
    @bot.command(description="Usage: !admin username")
    async def admin(ctx, user):
        
        global privilege_list
        
        if ctx.author.name in privilege_list:
            privilege_list = storage.privilege_add(user, privilege_list)
            await ctx.send(f" User {user} added to the list.")
        else:
            await ctx.send(f" You don't have the permition to use this")
   
    # --------------------------------------------------------
    
    # !deadmin
    @bot.command(description="Removes admin from user. Usage: !deadmin username")
    async def deadmin(ctx, user):
        
        global privilege_list
        
        if ctx.author.name in privilege_list:
            privilege_list = storage.privilege_remove(user, privilege_list)
            await ctx.send(f" User {user} removed from the list.")
        else:
            await ctx.send(f" You don't have the permition to use this")
   
   
    @bot.event
    async def on_ready():
        print('\n' + f'{bot.user.name} Starting up...') # print on terminal
        print(f'Token loaded.')
        
        global privilege_list 
        privilege_list = storage.privilege()
        print(f'Privilege list loaded with [{len(privilege_list)}] users.') 
        
        print(f'Commands loaded [{len(bot.commands)}].')
        
        print(f'Start up completed.\n')


    bot.run(TOKEN)
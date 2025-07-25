# CBot
WIP bot, don't touch

Discord bot with 3 commands:
  - hello (bot responds with "hey there *name*") 
  - roll (allows you to roll customizeble dice)
  - die (if you are the owner, the bot disconnect)

Discord bot invite [link](https://discord.com/api/oauth2/authorize?client_id=1173324757085724764&permissions=1084479765568&scope=bot)

## How to Compile localy
The bot needs Discord.py that can be found at: 
[pypi.org](https://pypi.org/project/discord.py/)

Or use the following commands in terminal:
```
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```

Now it's necessary to download the repository.
```
git clone https://github.com/lucaurssi/CBot.git
cd CBot/
```

And the last step, adding your discord token to the project.
[discord.com/developers/applications]{discord.com/developers/applications}
select "New Application".
Create your bot with image, name and whatever else you need.
when you are done, go to the 'Bot' category.
Look for the Token sub-category and reset the Token.
This new token can now be used when running this repository for the first time.

As a safety feature, the token file "token.clt" is selected by '.gitignore' so it doesn't go to github.

Run the repository with:
```
py main.py
```

With the bot runnning it will receive commands from any connected server.
To connect the bot to a server you need use the link in the 'Installation' section on the discord site linked above.

The step by step guide above was made in the 25th of july in 2025. 
The information may or may not be outdated.
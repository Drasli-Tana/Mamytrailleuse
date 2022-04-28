'''
Created on 28 avr. 2022

@author: Thomas
'''
import cogs.Spam as CM
import discord.ext.commands as DC
import json
import os

if __name__ == '__main__':
    if os.path.exists("data/config.json"):
        with open("data/config.json") as file:
            data = json.load(file)
    
    bot = DC.Bot(
        command_prefix=data.get("PREFIX", "$ "),
        case_insensitive = True)
    bot.add_cog(CM.Spam(bot))
    
    bot.run(data.get("TOKEN"))
    
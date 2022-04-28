"""
Created on 28 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC
import os
import json

class Munition(DC.Cog):
    """
    Un Cog qui ajoute une seule commande, pour spammer de pings un utilisateur
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        if os.path.exists("data/quotes.json"):
            with open("data/quotes.json") as file:
                self.quotes = json.load(file)
            
        else:
            self.quotes = list()
    
    @DC.command("fire")
    async def fire(self, ctx):
        print(ctx)
            
        
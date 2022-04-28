"""
Created on 28 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC
import os
import json
import random as RD

class Spam(DC.Cog):
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
    
    @DC.command("fire", help='Test', brief="Truc", usage="Temp")
    async def fire(self, ctx):
        """
        Envoie une quantité définie de Pings aux utilisateurs spécifiés
        """
        args = [arg 
                for arg in ctx.message.content.split(" ")[1:]
                if arg != '' and not arg.startswith("<@")]
        mentions = [mention for mention in ctx.message.mentions
                    if mention != self.bot.user]
        
        try:
            iterations = int(args[0])
        
        except (ValueError, IndexError):
            iterations = 1
            message = " ".join(args)
        
        else:
            message = " ".join(args[1:])
        
        if mentions:
            for mention in mentions + [ctx.message.author]:
                if mention.dm_channel is None:
                    await mention.create_dm()
            
            await ctx.message.author.dm_channel.send(
                f"Sending '{message}' {iterations} time(s) to " +
                f"{' '.join([mention.mention for mention in mentions])}")
            
            for mention in mentions:
                for message in (
                    [message if message != "" else RD.choice(self.quotes)
                    for _ in range(iterations)]):
                    await mention.dm_channel.send("*" + message + "*")
            
            await ctx.message.author.dm_channel.send("Done")
                
        else:
            await ctx.message.author.dm_channel.send("No user to ping")
            
        
"""
Created on 28 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC
import os
import json

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
    
    @DC.command("fire")
    async def fire(self, ctx):
        """
        Envoie une quantité définie de Pings aux utilisateurs spécifiés
        """
        args = ctx.message.content.split(" ")[1:]
        
        print(self.bot.get_user(599038518907502610))
        """
        if args:
            converter = DC.MemberConverter()
            target = await converter.convert(ctx, args[0])
            # Vérification de la cible
            # "Computer's lock"
            
            if target == self.user:
                await ctx.send("I can't target myself!" +
                               "I'm not a stormtrooper nor an elf!")
            
            else:
                await self.dmChannel(target)
                # Création du message privé (Cible)
                
                await self.dmChannel(ctx.message.author)
                # Création du retour (utilisateur)
                
                try:
                    iterations = int(args[1])
                
                except IndexError:
                    iterations = 1
                
                except ValueError:
                    iterations = 1
                
                try:
                    commentary = " ".join(args[2:])
                
                except IndexError:
                    commentary = "random commentary"
                                
                await ctx.message.author.dm_channel.send(
                    f"Sending '{commentary}' {iterations} time(s) " + 
                    f"to {target.mention}")
                
                with open("quotes.json") as file:
                    self.quotes = JS.load(file)["quotes"]
                
                for _ in range(iterations):
                    if commentary != "random commentary":
                        await target.dm_channel.send("*" + commentary + "*")
                    
                    else:
                        await target.dm_channel.send(
                            "*" + RD.choice(
                                self.quotes) + "*")
                
                await ctx.message.author.dm_channel.send("Done")
        else:
            await ctx.send("User not specified")
        """
        
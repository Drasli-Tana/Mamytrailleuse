import json as JS
import random as RD

import discord.ext.commands as DC

import HelpManager as HM
class Mitrailleuse(DC.Bot):
    def __init__(self):
        with open("config.json") as file:
            self.data = JS.load(file)
        # Loading *.json file with all bot info. 

        super().__init__(
            command_prefix = self.data["PREFIX"], case_insensitive = True,
            help_command=HM.HelpManager())
        
        self.commandHandler()
    
    def commandHandler(self):
        commandsNames = {
            "crash": self.crash,
            "fire":  self.fire}
        
        
        for cmd in commandsNames:
            commandData = self.data["commands"][cmd]
            command = DC.Command(
                commandsNames[cmd], name = cmd,
                help = ''.join(commandData["description"]),
                usage = commandData["syntax"],
                brief = commandData["short"])
            command.add_check(DC.check(self.isAdmin))
            
            self.add_command(command)
        
    def run(self):
        print("All wings report in.")
        super().run(self.data["TOKEN"])

    async def on_ready(self):
        print(f"[{self.user.name}] Standing by.")
    
    async def isAdmin(self, ctx):
        admin = await self.is_owner(ctx.message.author)
        if not admin:
            try: 
                admin = ctx.message.author.guild_permissions.administrator
            
            except AttributeError:
                admin = True
        
        return admin    
    
    async def crash(self, ctx):
        await ctx.send("It's a trap!")
        await self.close()
    
    async def dmChannel(self, target):
        if target.dm_channel is None:
            await target.create_dm()
    
    async def fire(self, ctx, *args):
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
        
    async def on_command_error(self, ctx, error):
        if isinstance(error, DC.errors.CheckFailure):
            author = ctx.message.author
            await self.createDm(author)
            
            await author.dm_channel.send(
                "Your lack of permissions is disturbing")
    

bot = Mitrailleuse()
bot.run()


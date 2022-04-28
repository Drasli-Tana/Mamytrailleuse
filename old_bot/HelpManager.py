'''
Created on 23 août 2021

@author: Thomas
'''

import discord.ext.commands as DC

class HelpManager(DC.DefaultHelpCommand):
    def __init__(self):
        super().__init__(
            dm_help=True, no_category="Commands", indent = 4,
            command_not_found="The {0} command is not in the main computer")
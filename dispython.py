

                                             ###############################################################################
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             #                              DISPYTHON                                      #
                                             #                                                                             #
                                             #                        VERSION CODE : 2.09.86                               #
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             ###############################################################################







import discord
from discord.ext import COMMANDS
import os



client = commands.Bot(command_prefix = 'd!')


@client.command()









### ON BOT Ready
@client.event
async def on_ready():
    print("bot cheese")



#BOT start
client.run(os.getenv("TOKEN"))



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
from discord.ext import commands
import os
import asyncio
import importlib
import file
import requests

global client
client = commands.Bot(command_prefix = 'd!')


async def run(ctx):
    try :
        importlib.reload(file)
        await file.script(ctx)

    except Exception as err:
        await ctx.send(str(err))



@client.command()
async def runcode(ctx):


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel



    await ctx.send("`Enter the entire code you want to test:`")

    try:
        scriptres = await client.wait_for("message", check = check, timeout = 300.0)

    except asyncio.TimeoutError:
        await ctx.send("`TimeOut`")
        return

    scriptlines = scriptres.content.split("\n")

    scriptfunc = "async def script(ctx):\n"

    for line in scriptlines:
        scriptfunc = scriptfunc + "    " + line + "\n"

    with open('file.py', 'w') as file:
        file.write(scriptfunc)

    asyncio.create_task(run(ctx))



### ON BOT Ready
@client.event
async def on_ready():
    print("bot cheese")



#BOT start
client.run(os.getenv("TOKEN"))

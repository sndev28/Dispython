

                                             ###############################################################################
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             #                              DISPYTHON                                      #
                                             #                                                                             #
                                             #                        VERSION CODE : 2.12.56                               #
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


async def run(ctx, client):
    try :
        importlib.reload(file)
        await file.script(ctx, client)

    except Exception as err:
        await ctx.send('```Error :\n' + str(err) + '```')



@client.command()
async def runcode(ctx):


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel



    await ctx.send("```Enter the entire code you want to test: (discord library and extensions are available by default. Import any other installed library you might need.)```")

    try:
        scriptres = await client.wait_for("message", check = check, timeout = 300.0)

    except asyncio.TimeoutError:
        await ctx.send("`TimeOut`")
        return

    if len(scriptres.attachments) != 0:
        script = requests.get(scriptres.attachments[0].url).text

    else :
        script = scriptres.content

    scriptlines = script.split("\n")

    scriptfunc = "import discord\nfrom discord.ext import commands\nasync def script(ctx, client):\n    try:\n"

    for line in scriptlines:
        scriptfunc = scriptfunc + "        " + line + "\n"

    scriptfunc = scriptfunc + "    except Exception as err:\n        await ctx.send(str(err))"

    with open('file.py', 'w') as file:
        file.write(scriptfunc)

    await ctx.send("```Running :```\n")

    asyncio.create_task(run(ctx,client))



### ON BOT Ready
@client.event
async def on_ready():
    print("bot cheese")



#BOT start
client.run(os.getenv('TOKEN'))

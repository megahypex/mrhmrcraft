import discord
import commands
from commandData import data as cmdata

#Data
smpuserpolicychannel = 795758489636306964
smpannouncements = 795733434860306482

smpverificationmsgid = 795760765872766996



prefix = cmdata().getPrefix()
commandData = cmdata().getData()
client = discord.Client(intent=discord.Intents.all())

def getRole(rolelist, name):
    return discord.utils.find(lambda r: r.name == name, rolelist)

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "type -smphelp for more info"))

@client.event
async def on_message(message):
    role = getRole(message.guild.roles, "SMP Member")

    
    if message.content.startswith(prefix):
        args = message.content.split()
        command = args[0].strip("-")

        if command in commandData:
            if not (role in message.author.roles):
                await commands.sendEmbed(discord, "Error", "You aren't an SMP Member", "", message.channel)
                return

            await commandData[command]["Run"](discord, client, message)

@client.event
async def on_raw_reaction_add(payload):

    if payload.message_id == smpverificationmsgid:
        if payload.emoji.name == "HMRCheckMark":
            await payload.member.add_roles(getRole(client.get_guild(payload.guild_id).roles, "Verified SMP Member"))



@client.event
async def on_raw_reaction_remove(payload):

   if payload.message_id == smpverificationmsgid:
        if payload.emoji.name == "HMRCheckMark":
            guild = await client.fetch_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id = payload.user_id)
            await member.remove_roles(getRole(client.get_guild(payload.guild_id).roles, "Verified SMP Member"))
client.run("ODA1NDYwNjcyNTMxMDA1NDkx.YBbNtQ.j9BQJuyrk4UFTSmRmOHb7NR_ySw") 
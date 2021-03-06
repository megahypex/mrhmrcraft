from os import path

#Utility
async def sendEmbed(ds, title, description, footer, channel):
    embed = ds.Embed(
        title = title,
        description = description,
        color = 0x440505
    )
    embed.set_footer(text = footer)
    await channel.send(embed = embed)

#Commands
async def status(ds, client, message):
   msg = path.exists("../../ServerStuff/Server/HMR Server/world/session.lock") and ":HMRCheckMark:795760765872766996 Online" or ":HMRXMark:805691417422462988 Offline"
   await sendEmbed(ds, "Server Status", msg, "Type -smphelp for a full list of commands", message.channel)

async def ip(ds, client, message):
    await sendEmbed(ds, "Server IPs", """
    **US Central** : 35.239.200.87
    """, "Other mirrors coming soon", message.channel)

async def smphelp(ds, client, message):
    from commandData import data 
    clss = data()
    commandData = clss.getData()
    prefix = clss.getPrefix()
    await sendEmbed(
        ds, 
        "Commands",
        f"""    
        **{prefix}status :** {commandData["status"]["Info"]}
        **{prefix}ip :** {commandData["ip"]["Info"]}
        **{prefix}smphelp :** {commandData["smphelp"]["Info"]}
        """,
        "",
        message.channel
    )
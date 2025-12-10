import os
import discord
import re

TOKEN = os.getenv("TOKEN")  # 這裡不用自己寫 Token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

x_url_pattern = re.compile(r"https?://(www\.)?x\.com/[\w\-/?=&%]+")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "x.com" in message.content:
        new_msg = message.content.replace("x.com", "vxtwitter.com")
        await message.channel.send(new_msg)

client.run(TOKEN)

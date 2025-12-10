import discord
import re
import os   # ← 你缺少這個，Railway 會直接爆掉

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

intents = discord.Intents.default()
intents.message_content = True  # 讀取訊息必須開啟
client = discord.Client(intents=intents)

# Regex：識別 X.com 的連結
x_url_pattern = re.compile(r"https?://(www\.)?x\.com/[\w\-/?=&%]+")

@client.event
async def on_message(message):
    # 避免 bot 重複回應自己
    if message.author == client.user:
        return

    # 如果訊息包含 x.com
    if "x.com" in message.content.lower():
        new_msg = message.content.replace("x.com", "vxtwitter.com")
        await message.channel.send(new_msg)

client.run(TOKEN)


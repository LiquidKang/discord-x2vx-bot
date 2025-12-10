import discord
import re

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # 要讀取訊息必開
client = discord.Client(intents=intents)

# Regex：找到 X.com/t... 這種類型的連結
x_url_pattern = re.compile(r"https?://(www\.)?x\.com/[\w\-/?=&%]+")

@client.event
async def on_message(message):
    # 避免 bot 回覆自己的訊息
    if message.author == client.user:
        return

    # 搜尋訊息中是否有 x.com 連結
    matches = x_url_pattern.findall(message.content)
    if "x.com" in message.content:
        # 替換成 vxtwitter.com
        new_msg = message.content.replace("x.com", "vxtwitter.com")
        await message.channel.send(new_msg)

client.run(TOKEN)

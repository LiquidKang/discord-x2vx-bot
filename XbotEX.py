import os
import discord
import re

# 取得環境變數 TOKEN
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Bot token not found! Please set the TOKEN environment variable.")

# 設定 Intents
intents = discord.Intents.default()
intents.message_content = True  # 必須開啟，才能讀取訊息內容

# 建立 Discord 客戶端
client = discord.Client(intents=intents)

# Regex：找到 x.com/t... 連結
x_url_pattern = re.compile(r"https?://(www\.)?x\.com/[\w\-/?=&%]+")

@client.event
async def on_ready():
    print(f"Bot 已登入: {client.user}")

@client.event
async def on_message(message):
    # 避免回覆自己
    if message.author == client.user:
        return

    # 搜尋訊息是否含有 x.com 連結
    if x_url_pattern.search(message.content):
        new_msg = x_url_pattern.sub(lambda m: m.group(0).replace("x.com", "vxtwitter.com"), message.content)
        await message.channel.send(new_msg)

# 啟動 Bot
client.run(TOKEN)

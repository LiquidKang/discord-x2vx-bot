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
intents.messages = True  # 確保可以讀取和刪除訊息

# 建立 Discord 客戶端
client = discord.Client(intents=intents)

# Regex：找到 x.com/t... 連結
x_url_pattern = re.compile(r"https?://(www\.)?x\.com/[\w\-/?=&%]+", re.IGNORECASE)

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
        # 逐個替換 X.com 為 vxtwitter.com
        def replace_x(match):
            url = match.group(0)
            return url.replace("x.com", "vxtwitter.com")
        
        new_msg = x_url_pattern.sub(replace_x, message.content)

        try:
            # 回覆 vxtwitter.com 連結
            await message.reply(new_msg, mention_author=False)
            # 刪除原本 X.com 訊息
            await message.delete()
        except discord.Forbidden:
            print("缺少刪除訊息的權限，請確認 bot 具有管理訊息或刪除訊息權限")
        except discord.HTTPException as e:
            print(f"刪除訊息或回覆時發生錯誤: {e}")

# 啟動 Bot
client.run(TOKEN)

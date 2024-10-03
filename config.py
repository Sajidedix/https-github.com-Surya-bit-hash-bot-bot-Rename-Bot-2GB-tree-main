import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "10658015")
    API_HASH  = os.environ.get("API_HASH", "a0087bca748f86698c53d291c9e5b3af")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7981857738:AAFvSoagF7lrOHNY-UVqyCE3kXLRk4Kqj2Y") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://helphm9:MO7vlO8DtXqezh3i@cluster0.mom8p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://i.ibb.co/PG890wf/image.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6170962395').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Renamechannel4") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002353049842"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Ｈᴇʟʟᴏ {} Ｂᴀʙᴜ 👋

➻ ɪ'ᴍ Ａᴅᴠᴀɴᴄᴇᴅ Ａɴᴅ Ｙᴇᴛ
   Ｐᴏᴡᴇʀғᴜʟ Ｒᴇɴᴀᴍᴇ Ｂᴏᴛ.
➻ Ｕsɪɴɢ Ｔʜɪs Ｂᴏᴛ Ｙᴏᴜ Ｃᴀɴ Ｒᴇɴᴀᴍᴇ
  Ａɴᴅ Ｃʜᴀɴɢᴇ Ｔʜᴜᴍʙɴᴀɪʟ Ｏғ Ｙᴏᴜʀ Ｆɪʟᴇs.
➻ Ｙᴏᴜ Ｃᴀɴ Ａʟsᴏ Ｃᴏɴᴠᴇʀᴛ Ｖɪᴅᴇᴏ
   Ｔᴏ Ｆɪʟᴇ Ａɴᴅ Ｆɪʟᴇ Ｔᴏ Ｖɪᴅᴇᴏ.
➻ ɪ'ᴍ Ａʟsᴏ Ｓᴜᴘᴘᴏʀᴛᴇ Ｃᴜsᴛᴏᴍ
   Ｔʜᴜᴍʙɴᴀɪʟ Ａɴᴅ Ｃᴜsᴛᴏᴍ Ｃᴀᴘᴛɪᴏɴ.
"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 Ｍʏ Ｎᴀᴍᴇ</b> : {}
├<b>🖥️ Ｄᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href=http://t.me/GaaraFx>Ｓᴀᴊɪᴅ</a> 
├<b>📕 Ｌɪʙʀᴀʀʏ</b> : <a href=https://github.com/pyrogram>Ｐʏʀᴏɢʀᴀᴍ</a>
├<b>✏️ Ｌᴀɴɢᴜᴀɢᴇ</b> : <a href=https://www.python.org>Ｐʏᴛʜᴏɴ 𝟹</a>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

Ａɴʏ Ｏᴛʜᴇʀ Ｈᴇʟᴘ Ｃᴏɴᴛᴀᴄᴛ :- <a href=http://t.me/GaaraFx>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Ｔʜᴀɴᴋs Ｆᴏʀ Ｓʜᴏᴡɪɴɢ Ｉɴᴛᴇʀᴇsᴛ Ｉɴ Ｄᴏɴᴀᴛɪᴏɴ! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `8175851962@ybl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @NarutoPublicST</code>

💬 Ｆᴏʀ Ａɴʏ Ｈᴇʟᴘ Ｃᴏɴᴛᴀᴄᴛ @GaaraFx
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper

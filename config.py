import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "10658015")
    API_HASH  = os.environ.get("API_HASH", "a0087bca748f86698c53d291c9e5b3af")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7981857738:AAFvSoagF7lrOHNY-UVqyCE3kXLRk4Kqj2Y") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sand43729:XGZAz0ovV6wRAwFs@cluster0.gjhmd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://ibb.co/vLQ8s3j")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6170962395').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "NarutoPublicST") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002353049842"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hy {} Bᴀʙᴜ 🫠
╭────────────⋗
├⋗ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ
├⋗ ᴘᴏᴡᴇƦҒᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.
├⋗ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ sᴇᴛ
├⋗ ᴛʜᴜᴍʙɴᴀɪʟ ᴏғ ʏᴏᴜʀ ғɪʟᴇs.
├⋗ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ
├⋗ ᴛᴏ ғɪʟᴇ ᴀɴᴅ ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.
╰─────────────────⋗
"""

    ABOUT_TXT = """
╭───────────⋗
├⋗<b>🤖 Mʏ Nᴀᴍᴇ</b> : {}
├⋗<b>🖥️ Dᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href=http://t.me/GaaraFx>Sᴀᴊɪᴅ</a> 
├⋗<b>📕 Lɪʙʀᴀʀʏ</b> : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├⋗<b>✏️ Lᴀɴɢᴜᴀɢᴇ</b> : <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a>     
╰─────────────────⋗
"""

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
  
➪ /start - Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴʏ Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ.
➪ /del_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ.
➪ /view_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ.

📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</u></b>

➪ /set_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /see_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /del_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ Exᴀᴍᴘʟᴇ - <code>/Sᴇᴛ_Cᴀᴘᴛɪᴏɴ 📕 Nᴀᴍᴇ ➠ : {filename}

🔗 Sɪᴢᴇ ➠ : {filesize} 

⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}</code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>

➪ Sᴇɴᴛ Aɴʏ Fɪʟᴇ Aɴᴅ Tʏᴘᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ Aɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ Dᴏᴄᴜᴍᴇɴᴛ, Vɪᴅᴇᴏ, Aᴜᴅɪᴏ ].           

Aɴʏ Oᴛʜᴇʀ Hᴇʟᴘ Cᴏɴᴛᴀᴄᴛ :- <a href=http://t.me/GaaraFx>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Sɪᴢᴇ :</b> {1} | {2}
️ <b>⏳️ Dᴏɴᴇ :</b> {0}%
 <b>🚀 Sᴘᴇᴇᴅ :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>

ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟷𝟶 ʀs ᴜᴘᴛᴜ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

<b>🛍 UPI ID:</b> `sajideditz27@okhdfcbank`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

ғᴏʀ ᴇxᴀᴍᴘʟᴇ! 

<code>By ❃ @NarutoPublicST</code>

💬 ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ @GaaraFx
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper

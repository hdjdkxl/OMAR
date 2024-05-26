from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

app = Client("leave", api_id=122000, api_hash="de9a2f1c8734b48f5",
             bot_token="6246284893:AAHCh81a-g")

OWNER = 833360381  #ایدیك

@app.on_message(filters.command('leave') & filters.user(OWNER))
async def leave_a_chat(client, message):
    if len(message.command) == 1: return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ɢʀᴏᴜᴘ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url=f'https://t.me/MGIMT')]]
        await client.send_message(chat_id=chat,
                                  text='<b>Hᴇʟʟᴏ Fʀɪᴇɴᴅs, \nMʏ Aᴅᴍɪɴ Hᴀs Tᴏʟᴅ Mᴇ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ Gʀᴏᴜᴘ Sᴏ I Gᴏ! Iғ Yᴏᴜ Wᴀɴɴᴀ Aᴅᴅ Mᴇ Aɢᴀɪɴ Cᴏɴᴛᴀᴄᴛ Mʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</b>',
                                  reply_markup=InlineKeyboardMarkup(buttons))
        await client.leave_chat(chat)
    except Exception as e:
        await message.reply(f'Eʀʀᴏʀ: {e} ')

print("✔")
app.run()

##طریقه تشغیل :
## /leave @usergroup او id group
###@IQ7amo dev
### @MGIMT مصدري

## یمکن شغل من بوت اغاني یوکي او انوکس
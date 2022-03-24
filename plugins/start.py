from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_photo(
            photo="https://telegra.ph/file/70d2da745d72f8ecdf141.jpg"
            caption=f"""Hello {message.from_user.mention}🤠
<b>മലയാളം സിനിമാ ചാനൽ ലിസ്റ്റ് ബോട്ടിലേക്ക് സ്വാഗതം,
⭕Creator:</b> <a href='https://t.me/Mccontact_bot'>👤This Person</a>
⭕Channel:</b> <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>Click Here</a>
⭕How To Download Movies? :</b> <a href='https://t.me/malyalamcinemass/23'>Click Me</a>
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Channel 🇮🇳" ,url="https://t.me/+slPWoPDfoJc3NTVl"), 
	  InlineKeyboardButton("Subscribe 🧐", url="https://t.me/mc_cinema")
          ],[
          InlineKeyboardButton("🧩 Series 🧩", url="https://t.me/mc_serie")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))

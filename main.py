import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random



api_id = 13482338
api_hash = "f2839ec661fb8d7f318f3dec05b8bf8f"
 
app = Client("my_account", api_id, api_hash)
 
# type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            sleep(1)

# heart
@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def heart(_, msg):
    time = 1
    msg.edit("❤️")
    sleep(time)
    msg.edit("🧡")
    sleep(time)
    msg.edit("💛")
    sleep(time)
    msg.edit("💚")
    sleep(time)
    msg.edit("💙")
    sleep(time)
    msg.edit("💜")
    sleep(time)
    msg.edit("🖤")
    sleep(time)
    msg.edit("🤍")
    sleep(time)
    msg.edit("❤️")
#infinityheart
@app.on_message(filters.command("infheart", prefixes=".") & filters.me)
def infheart(_, msg):
    time = 3.42
    try:
        while(True):
            msg.edit("❤️")
            sleep(time)
            msg.edit("🧡")
            sleep(time)
            msg.edit("💛")
            sleep(time)
            msg.edit("💚")
            sleep(time)
            msg.edit("💙")
            sleep(time)
            msg.edit("💜")
            sleep(time)
            msg.edit("🖤")
            sleep(time)
            msg.edit("🤍")
            sleep(time)
    except FloodWait as e:
            sleep(1)


# font

@app.on_message(filters.command("font", prefixes=".") & filters.me)
def typee(_, msg):
    orig_text = msg.text.split(".font ", maxsplit=1)[1]
    text = orig_text
#    text.setFont("Times", 8)
    msg.edit(text)

# change 
REPLACEMENT_MAP = {
    "a":"𝖆",
    "b":"𝖇",
    "c":"𝖈",
    "d":"𝖉",
    "e":"𝖊",
    "f":"𝖋",
    "g":"𝖌",
    "h":"𝖍",
    "i":"𝖎",
    "j":"𝖏",
    "k":"𝖐",
    "l":"𝖑",
    "m":"𝖒",
    "n":"𝖓",
    "o":"𝖔",
    "p":"𝖕",
    "q":"𝖖",
    "r":"𝖗",
    "s":"𝖘",
    "t":"𝖙",
    "u":"𝖚",
    "v":"𝖛",
    "w":"𝖜",
    "x":"𝖝",
    "y":"𝖞",
    "z":"𝖟",
    "A":"𝕬",
    "B":"𝕭",
    "C":"𝕮",
    "D":"𝕯",
    "E":"𝕰",
    "F":"𝕱",
    "G":"𝕲",
    "H":"𝕳",
    "I":"𝕴",
    "J":"𝕵",
    "K":"𝕶",
    "L":"𝕷",
    "M":"𝕸",
    "N":"𝕹",
    "O":"𝕺",
    "P":"𝕻",
    "Q":"𝕼",
    "R":"𝕽",
    "S":"𝕾",
    "T":"𝕿",
    "U":"𝖀",
    "V":"𝖁",
    "W":"𝖂",
    "X":"𝖃",
    "Y":"𝖄",
    "Z":"𝖅"
}



@app.on_message(filters.command("change", prefixes=".") & filters.me)
def change(_, msg):
    text = msg.text.split(".change ", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)




app.run()
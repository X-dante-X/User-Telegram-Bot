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
    tbp = ""
    typing_symbol = "โ"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            sleep(1)


#infinitytype
@app.on_message(filters.command("inftype", prefixes=".") & filters.me)
def infl(_, msg):
    orig_text = msg.text.split(".inftype ", maxsplit=1)[1]
    inftext = orig_text
    text = orig_text
    tbp = ""
    typing_symbol = "โ"
    while(True):
        while(tbp != orig_text):
            try:
                msg.edit(tbp + typing_symbol)
                sleep(0.5)
        
                tbp = tbp + text[0]
                text = text[1:]
        
                msg.edit(tbp)
                sleep(0.5)
            except FloodWait as e:
                sleep(8)
        sleep(1)
        tbp = ""
        text = inftext
        




# heart
@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def heart(_, msg):
    time = 1
    msg.edit("โค๏ธ")
    sleep(time)
    msg.edit("๐งก")
    sleep(time)
    msg.edit("๐")
    sleep(time)
    msg.edit("๐")
    sleep(time)
    msg.edit("๐")
    sleep(time)
    msg.edit("๐")
    sleep(time)
    msg.edit("๐ค")
    sleep(time)
    msg.edit("๐ค")
    sleep(time)
    msg.edit("โค๏ธ")

#infinityheart
@app.on_message(filters.command("infheart", prefixes=".") & filters.me)
def infheart(_, msg):
    time = 3.42
    try:
        while(True):
            msg.edit("โค๏ธ")
            sleep(time)
            msg.edit("๐งก")
            sleep(time)
            msg.edit("๐")
            sleep(time)
            msg.edit("๐")
            sleep(time)
            msg.edit("๐")
            sleep(time)
            msg.edit("๐")
            sleep(time)
            msg.edit("๐ค")
            sleep(time)
            msg.edit("๐ค")
            sleep(time)
    except FloodWait as e:
            sleep(8)


# font

@app.on_message(filters.command("font", prefixes=".") & filters.me)
def typee(_, msg):
    orig_text = msg.text.split(".font ", maxsplit=1)[1]
    text = orig_text
#    text.setFont("Times", 8)
    msg.edit(text)

# change 
REPLACEMENT_MAP = {
    "a":"๐",
    "b":"๐",
    "c":"๐",
    "d":"๐",
    "e":"๐",
    "f":"๐",
    "g":"๐",
    "h":"๐",
    "i":"๐",
    "j":"๐",
    "k":"๐",
    "l":"๐",
    "m":"๐",
    "n":"๐",
    "o":"๐",
    "p":"๐",
    "q":"๐",
    "r":"๐",
    "s":"๐",
    "t":"๐",
    "u":"๐",
    "v":"๐",
    "w":"๐",
    "x":"๐",
    "y":"๐",
    "z":"๐",
    "A":"๐ฌ",
    "B":"๐ญ",
    "C":"๐ฎ",
    "D":"๐ฏ",
    "E":"๐ฐ",
    "F":"๐ฑ",
    "G":"๐ฒ",
    "H":"๐ณ",
    "I":"๐ด",
    "J":"๐ต",
    "K":"๐ถ",
    "L":"๐ท",
    "M":"๐ธ",
    "N":"๐น",
    "O":"๐บ",
    "P":"๐ป",
    "Q":"๐ผ",
    "R":"๐ฝ",
    "S":"๐พ",
    "T":"๐ฟ",
    "U":"๐",
    "V":"๐",
    "W":"๐",
    "X":"๐",
    "Y":"๐",
    "Z":"๐"
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
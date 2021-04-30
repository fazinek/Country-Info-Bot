# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Country-Info-Bot/blob/main/LICENSE

import os
import pyrogram
import asyncio
import time
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

Ekbotz = Client(
    "Country Info Search Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """
<b>Hello 👋</b> {}, 
<b>I Am A Country Info Provider Bot. I Can Find Informations About All Countries. Do You Have Any Doubts❓ Use Buttons Below 😅. 
<u>Give me a country name I will send the informations of that country</u>.</b>

Please Join My Update Channel For Know More @eKbOtZ_upDaTE.</b>
"""
HELP_TEXT = """
• Just send me a country name
• Wait Few Seconds 😂
• Then I will check and send you the informations
"""
INFO_TEXT = """
<b><u>Informations :-</u></b>
There Is The List Of That I Can Fetch These Informations👇.
Name, Native Name, Capital, Population, Region, Sub Region, Top Level Domains, Calling Codes, Currencies, Residence, Timezone, Wikipedia, Google

<b>A Bot From @eKbOtZ_upDaTE</b>
"""
ABOUT_TEXT = """
- **Bot :** `Country Info Search Bot`
- **Channel :** [EK BOTZ PROJECTS](https://telegram.me/eKbOtZ_upDaTE)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚜️ Channel ⚜️', url='https://telegram.me/eKbOtZ_upDaTE'),
        InlineKeyboardButton('💬 Feedbacks 💬', url='https://telegram.me/Feedback_ek_bot')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@Ekbotz.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@Ekbotz.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@Ekbotz.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=INFO_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
@Ekbotz.on_message(filters.private & filters.command(["info"]))
async def info(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@Ekbotz.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    country = CountryInfo(update.text)
    info = f"""
Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Prime Minister : `{country.prime_minister()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Number States : `{country.number_states()}`
Country Domains : `{country.tld()}`
Country Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`
"""
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country.name()}')
        ],[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')

        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except FloodWait as floodwait:
        await asyncio.sleep(floodwait.x)
        return countryinfo(bot, update)
    except KeyError as keyerror:
        print(keyerror)
    except Exception as error:
        print(error)

EkBotz.run()

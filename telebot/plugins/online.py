# Copyright TeleBot
# For @TeleBotHelp coded by @xditya
# Kangers keep credits else I'll take down 🧐

import random
import sys

from telethon import version

from telebot import ALIVE_NAME
from telebot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TeleBot User"

ONLINESTR = [
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**GamerzBot is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [GAMERFUCKER](tg://user?id=1209574071) \n\n**More help -** @Gamerzbots \n\n           [🚧 GitHub Repository 🚧](https://github.com/gamerfuckerofficial/Gamerzbot)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to Gamerzbot**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @Gamerzbots \n\n✔️ Created by: [GAMERFUCKER](tg://user?id=1209574071) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/gamerfuckerofficial/Gamerzbot)",
]


@telebot.on(admin_cmd(outgoing=True, pattern="online"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))

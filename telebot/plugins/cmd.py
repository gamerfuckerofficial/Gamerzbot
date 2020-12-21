import time

import asyncio

import os

from telethon import events

from telethon.tl import functions, types

@telebot.on(admin_cmd(outgoing=True, pattern="cmd"))

async def install(event):

    if event.fwd_from:

        return

    cmd = "ls telebot/plugins/*.py"

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    stdout, stderr = await process.communicate()

    o = stdout.decode()

    _o = o.split("\n")

    o = "\n".join(_o)

    OUTPUT = f"**LIST OF PLUGINS IN MastUserBot🔍:**\n{o}\n\n**TIP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All plugins might not work directly.__"

    await event.edit(OUTPUT)

"""Plugin to get the video tutorial to deploy TeleBot
.tut"""

from telebot.utils import admin_cmd


@telebot.on(admin_cmd(outgoing=True, pattern="tut"))
async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit(
            "Get a userbot like mine!! Watch [this video tutorial](https://t.me/Gamerzbots) on deploying..."
        )

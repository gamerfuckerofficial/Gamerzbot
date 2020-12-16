from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(outgoing=True, pattern="group"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(
            e,
            "This is my community.\n\n[Channel](http://t.me/Gamerzbots)\n\n[Chat Group](https://t.me/miakhalifachatgroup)\n\n[UserBot Tutorial - GamerzBot](https://t.me/Gamerzbots)\n\n[GamerzBot Chat](https://t.me/miakhalifachatgroup)\n\n[Github](https://github.com/gamerfuckerofficial)\n\n[YouTube](https://youtube.com/channel/UCOAKFN1uKUhSYcnrQhytBng)",
        )


CMD_HELP.update({"group": ".group\nUse - None."})

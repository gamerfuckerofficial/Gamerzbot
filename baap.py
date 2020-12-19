from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd

from telebot import CMD_HELP


@telebot.on(admin_cmd(pattern="baap"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Beta baap se bakchodi nahi samjha na warna chut mai talwar daalunga ,gand mai jhaadu daalke mor banaunga bhaag bhadve chut maaru  teri maa ki chut mai chappal,ghoda,danda,pathar,wire,giraffe,tiger,talwar Teri maa ko deepak kalal teri maa ko johny bhaiya teri maa ko mai , neta neta har koi kehta tisri manjil pe rehta teri maa ko chodu gand marne jaisa ,tera baap bajaye dol teri maa bajaye pungi teri behen nache nangi usko chode saare bhangi ???不,teri maa meri fan ,teri maa meri randi ,teri maa ko negro, bhadve nikal teri maa nangi karke chodunga samjha bhadva saala,chudne ka shok hai kya tujhe bete aisa chodunga na ghar tak bache dete jayegi tu bhaag madharchod!"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


CMD_HELP.update({"baap": ".baap\nUse - Long abuse, in hindi."})

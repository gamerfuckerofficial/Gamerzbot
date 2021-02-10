# GamerzBot - Telegram UserBot

# <p align="left"><a href="https://github.com/gamerfuckerofficial/Gamerzbot"><img src="https://github-readme-stats.vercel.app/api/pin?username=gamerfuckerofficial&show_icons=true&theme=dark&hide_border=true&repo=Gamerzbot"></a></p><p align="centre"><a href="https://t.me/miakhalifachatgroup"> <img src="https://img.shields.io/badge/telegram-Support_Group-blue?style=social&logo=telegram" alt="Support" /></a><a href="https://github.com/gamerfuckerofficial/Gamerzbot/stargazers"><img src="https://img.shields.io/github/stars/gamerfuckerofficial/Gamerzbot?style=social"></a><a href="https://github.com/gamerfuckerofficial/Gamerzbot/fork"><img src="https://img.shields.io/github/forks/gamerfuckerofficial/Gamerzbot?label=Fork&logoColor=blue&style=social"></a>	<a href="https://github.com/gamerfuckerofficial/Gamerzbot"><img src="https://img.shields.io/github/last-commit/gamerfuckerofficial/Gamerzbot?style=flat-square"></a></p>
    
## Video Tutorial on deploying

Click the below button to watch the video tutorial on deploying

<a href="soon"><img src="https://img.shields.io/badge/How%20To%20Deploy-LATEST-blue.svg?logo=Youtube"></a>
<a href="soon"><img src="https://img.shields.io/youtube/views/aPU334icQSM?style=social">
    
<a href="soon"><img src="https://img.shields.io/badge/How%20To%20Deploy-OLD-blue.svg?logo=Youtube"></a>
<a href="soon"><img src="https://img.shields.io/youtube/views/XmvdDHiIDb4?style=social"></a>
    
    
## Documentation
For passionate readers 😂 the documentation can be found [here](https://github.com/gamerfuckerofficial/Gamerzbot)

## The Easier Way to install

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gamerfuckerofficial/Gamerzbot)

## Support
Join [Gamerz Bot support](https://t.me/Gamerzbots) for updates and new plugin suggestions.
Do fork and star the repo 

### Session String 
<a href="https://repl.it/@gamerfuckeroffi/Gamerzbot" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/gamerfuckerofficial/Gamerzbot
cd Gamerzbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m telebot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Check [Line 111](https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/uniborgConfig.py#L111) and start adding your vars there.
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

## Credits t.me/xditya

# Disclaimer
```
/**
    	Improper use may lead to ban.
    	I am not responsible if you misuse this bot.
	This bot is just for managing groups more effectively and having some fun
	with your telegram account.
	No one is responsible for your actions.
	If you spammed and got reported again and again, 
	and, at last got your account banned, and you
	point your fingers at me, I'll be rolling on the floor laughing at you.
/**
```


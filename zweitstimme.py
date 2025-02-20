import requests as re
import json
from datetime import datetime
import telebot
import os

os.chdir(os.getcwd())

try:
    zweit_resp = re.get("https://polsci.uni-wh.de/forecast", verify=False)
    zweit_content = json.dumps(json.loads(zweit_resp.content))

    erst_resp = re.get("https://polsci.uni-wh.de/forecast_districts", verify=False)
    erst_content = json.dumps(json.loads(erst_resp.content))

    for file, name in zip([zweit_content, erst_content], ["zweit_content", "erst_content"]):
        with open(f'data/{name}_{datetime.now().isoformat()[:-10]}.json', 'w') as f:
            f.write(file)
except Exception as e:
    bot = telebot.TeleBot(os.environ['token'])
    bot.send_message(os.environ['chat_id'], f'Error! \n {e}')
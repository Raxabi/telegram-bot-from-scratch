# TELEGRAM BOT USING THE API

import requests as req
from dotenv import load_dotenv, get_key
from pprint import pprint
import re
import os

config = load_dotenv(".env")

teletoken = os.environ.get("telegram_token")

chat_id = os.environ.get("chat_id")

uri = f"https://api.telegram.org/bot{teletoken}/"

# Dynamic Telegram API method
def method(method):
    return f"{uri}{method}"

# Response to a command

#pprint(req.post(method("getChat"), data={"chat_id": "@ekisdelol"}).json())

update_id = []
def listen_bot_on_chat(chat_id: str or int):
    
    # Get updates
    updates = req.get(method("getUpdates"))
    response = updates.json()

    global update_id

    if len(update_id) == 0:
        update_id.append(response["result"][-1]["update_id"])

    if response["result"][-1]["update_id"] != update_id[-1]:
        update_id.append(response["result"][-1]["update_id"])

    # data to parse in the if control
    command_regex = re.findall("^/text*", response["result"][-1]["message"]["text"])

    if command_regex == ["/text"] and len(update_id) == 1:
        print(response["result"][-1]["update_id"], update_id[-1])
        if response["result"][-1]["update_id"] != update_id[-1]:
            req.post(method("sendMessage"), data={"chat_id": chat_id, "text": "Example text"})
            print("Nueva peticion de:", response["result"][-1]["message"]["from"]["first_name"], "\n", "Peticion:", response["result"][-1]["message"]["text"])


if __name__ == "__main__":
    print("Bot listening on chat")
    while True:
        listen_bot_on_chat(chat_id)
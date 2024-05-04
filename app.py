import logging
import os
import re
import ssl
import certifi

from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# ----------- 動かすための準備 -----------
# ※ここは変更しないでください
load_dotenv()
logging.basicConfig(level=logging.DEBUG)
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token=os.getenv("BOT_TOKEN"), ssl=ssl_context)
app = App(token=os.environ.get("BOT_TOKEN"), client=client)
# ----------- 動かすための準備 -----------


@app.message("やっほー")
def message_echo(message, say):
    say("やっほー！！！")


@app.message(re.compile("こだま (.*)"))
def message_(say, context):
    text = context["matches"][0]
    say(text)


# ----------- 動かすための準備 -----------
# ここも変更しないでください
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("APP_TOKEN"))
    handler.start()
# ----------- 動かすための準備 -----------

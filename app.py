import logging
import os
import re
import ssl
import certifi

from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# ⚠️ここは変更しないでください
load_dotenv()
logging.basicConfig(level=logging.DEBUG)
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token=os.getenv("BOT_TOKEN"), ssl=ssl_context)
app = App(token=os.environ.get("BOT_TOKEN"), client=client)
# ----------- 動かすための準備 ここまで -----------


# "やっほー"というメッセージに対して"やっほー！！！"と返します
@app.message("やっほー")
# 👆👆 "やっほー"の部分を変えると、変更後のメッセージに対して返信します
def message_echo(message, say):
    say("やっほー！！！")
    # 👆👆 ここで返信するメッセージを決めています
    # この場合、"やっほー！！！"と返信します


# 「こだま ○○」に対して「○○」と返します
@app.message(re.compile("こだま (.*)"))
# 👆👆 (.*) の部分にはどんな文章でも入ります
def message_(say, context):
    text = context["matches"][0]
    # 👆👆 こうすると「こだま ○○」の○○の部分を取り出せます
    say(text)


# ここから下に新しい処理を追加していってください
# いろんな処理を追加して，SlackBotをカスタマイズしていきましょう！


# ----------- 動かすための準備2 ここから -----------
# ⚠️ここも変更しないでください
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("APP_TOKEN"))
    handler.start()

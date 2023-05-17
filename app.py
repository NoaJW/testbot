from flask import Flask, request
import telegram
import os
import re
from sgchattingbot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# start the flask app
app = Flask(__name__)


@app.route('/6207929876:AAGLcN0irRbfZFi27b7jFEDJfUprStJPy6M', methods=['POST'])   # POST to /{token}
def test_token():
    return "okok"


# @app.route('/{}'.format(TOKEN), methods=['POST'])   # POST to /{token}
# def respond():
#     # retrieve the message in JSON and then transform it to Telegram object
#     update = telegram.Update.de_json(request.get_json(force=True), bot)

#     chat_id = update.message.chat.id
#     msg_id = update.message.message_id

#     # Telegram understands UTF-8, so encode text for unicode compatibility
#     text = update.message.text.encode('utf-8').decode()
#     # for debugging purposes only
#     print("got text message :", text)

#     # start point when user intiates chat with bot
#     if text == "/start":
#         # welcome message
#         bot_welcome = """
#        Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
#        """
#         # send the welcome message
#         bot.sendMessage(chat_id=chat_id, text=bot_welcome,
#                         reply_to_message_id=msg_id)
#     else:
#         try:
#             # clear the message we got from any non alphabets
#             text = re.sub(r"\W", "_", text)
#             # create the api link for the avatar based on http://avatars.adorable.io/
#             url = "https://api.adorable.io/avatars/285/{}.png".format(
#                 text.strip())
#             # reply with a photo to the name the user sent,
#             # note that you can send photos by url and telegram will fetch it for you
#             bot.sendPhoto(chat_id=chat_id, photo=url,
#                           reply_to_message_id=msg_id)
#         except Exception:
#             bot.sendMessage(
#                 chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

#     return 'ok'



@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')     # homepage
def index():
    return 'home'


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)

    


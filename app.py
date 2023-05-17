from flask import Flask, request
import telegram
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters
import os
import re
from sgchattingbot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# start the flask app
app = Flask(__name__)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# # Create the handlers
# start_handler = CommandHandler('start', start)
# # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)


# # Create updater
# updater = Updater(bot)

# # Register handlers with the Dispatcher of the Updater 
# dispatcher = updater.dispatcher
# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(echo_handler)

# # Start bot
# updater.start_polling()

# # Run bot
# updater.idle()


def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start_handler))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == '__main__':
    main()

    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)

    


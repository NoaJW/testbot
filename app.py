from telegram.ext import CommandHandler, Updater
from logging import basicConfig, getLogger, INFO

BOT_TOKEN = "6207929876:AAGLcN0irRbfZFi27b7jFEDJfUprStJPy6M"

basicConfig(level=INFO)
log = getLogger()

def start(update, context):
    update.message.reply_text(
        "start this bot",
        parse_mode="markdown")

def help(update, context):
    update.message.reply_text(
        "help for this bot",
        parse_mode="markdown")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()
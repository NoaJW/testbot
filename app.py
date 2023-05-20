from telegram.ext import CommandHandler, Updater
from logging import basicConfig, getLogger, INFO
import waitress

BOT_TOKEN = "6207929876:AAF6QVdvg8SwscPh1gbd_BwE2rqX0re-L3g"

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


def application(environ, start_response):
    # Your WSGI application logic here
    main()

    # Set the response status and headers
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    # Start the response using the start_response callable
    start_response(status, headers)

# if __name__ == '__main__':
#     waitress.serve(application, host='0.0.0.0', port=8080)
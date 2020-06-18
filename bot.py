from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
from telegram.ext import Updater
from assignments import assignment as countAssignment
import quickstart

updater = Updater(
    token='', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")

def assignment(update,context):
    quickstart.checkmail()
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(countAssignment()))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

assignment_handler = CommandHandler('assignment',assignment)
dispatcher.add_handler(assignment_handler)


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.idle()

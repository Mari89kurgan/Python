from bot_commands import *
from telegram.ext import Updater, CommandHandler

if __name__ == '__main__':
    updater = Updater('5584902301:AAFNSeLzUhcCU9qibucFVKEvCxaEhVJAVHM')
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('cost', cost_money))
    print('\nStart server.........')
    updater.start_polling()
    updater.idle()

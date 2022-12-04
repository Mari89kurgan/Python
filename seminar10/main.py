from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from bot_func import start_command, callback, controller

if __name__ == '__main__':
    updater = Updater('5584902301:AAFNSeLzUhcCU9qibucFVKEvCxaEhVJAVHM', use_context=True)
    dispatcher = updater.dispatcher

    start_command_handler = CommandHandler('start', start_command)
    button = MessageHandler(Filters.regex(''), controller)
    callback_button_handler = CallbackQueryHandler(callback=callback, pattern=None, run_async=False)

    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(callback_button_handler)
    dispatcher.add_handler(button)

    print('\nStart server.........')
    updater.start_polling()
    updater.idle()

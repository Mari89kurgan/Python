import requests
from telegram import Update
from telegram.ext import CallbackContext


def log(update: Update, context: CallbackContext):
    with open('logger.csv', 'a', encoding='utf-8') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/cost - цена валюты\n/help - все команды\n')


def cost_money(update: Update, context: CallbackContext):
    log(update, context)
    my_reg = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = my_reg.json()
    money_list = [i for i in data.get('Valute')]
    msg = update.message.text
    items = msg.split()
    x = items[1].upper()
    if x in money_list:
        update.message.reply_text(data.get('Valute').get(x).get('Value'))
    else:
        update.message.reply_text('Нет такой валюты')

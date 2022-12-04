import telegram
from telegram.ext import CallbackContext
import calc_rational_num
import calc_complex_num
from logger import logger


ask_1 = 1


def start_command(update: telegram.Update, contex: CallbackContext):
    button_a = telegram.InlineKeyboardButton('Рациональные числа', callback_data='button_a')
    button_b = telegram.InlineKeyboardButton('Комплексные числа', callback_data='button_b')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[button_a], [button_b]])

    update.message.reply_text('Привет. Это калькулятор. Выберите действие: ', reply_markup=markup)

    return callback


def callback(update: telegram.Update, contex: CallbackContext):
    global ask_1
    query = update.callback_query
    variant = query.data
    if variant == 'button_a':
        query.answer()
        query.edit_message_text(text="Введите через пробел два рациональных числа и действие ('+', '-', '*', '/')")

    elif variant == 'button_b':
        query.answer()
        query.edit_message_text(text="Введите через пробел два комплексных числа и действие ('+', '-', '*', '/')")
        ask_1 = 2


def controller(update: telegram.Update, contex: CallbackContext):
    msg = update.message.text.split()
    ask_2 = msg[2]
    answer = msg[:2]
    if ask_1 == 1:
        if ask_2 == '+':
            res = calc_rational_num.addition(answer)
        elif ask_2 == '-':
            res = calc_rational_num.subtraction(answer)
        elif ask_2 == '*':
            res = calc_rational_num.multiplication(answer)
        else:
            res = calc_rational_num.division(answer)
    else:
        if ask_2 == '+':
            res = calc_complex_num.addition(calc_complex_num.get_part(answer))
        elif ask_2 == '-':
            res = calc_complex_num.subtraction(calc_complex_num.get_part(answer))
        elif ask_2 == '*':
            res = calc_complex_num.multiplication(calc_complex_num.get_part(answer))
        else:
            res = calc_complex_num.division(calc_complex_num.get_part(answer))
    logger(ask_1, ask_2, answer, res)
    update.message.reply_text(f'{res}')

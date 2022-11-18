from view import type_num, action, input_num
import calc_rational_num
import calc_complex_num
from logger import logger


def controller():
    ask_1 = type_num()
    ask_2 = action()
    answer = input_num()
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
    print('Результат вычислений:', res)
    return res

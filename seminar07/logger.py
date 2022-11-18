from datetime import datetime


def logger(type_num, action, input_num, result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{curr_time}\t{type_num}\t{action}\t{input_num}\t{result}\n'.format(
            curr_time=datetime.now(),
            type_num=dict_num.get(type_num),
            action=action,
            input_num=input_num,
            result=result
        ))


dict_num = {1: 'комплексные числа', 2: 'рациональные'}

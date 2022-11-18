def type_num():
    action_lisr = [1, 2]
    while True:
        ask_type = int(input('\nC какими числа будем работать (1 - рациональными, 2 - комплексными): '))
        if ask_type in action_lisr:
            break
    return ask_type


def action():
    action_lisr = ['+', '-', '*', '/']
    ask_action = input('Какое выполнить действие ("+", "-", "*", "/"): ')
    while True:
        if ask_action in action_lisr:
            break
    return ask_action


def input_num():
    numbers_list = []
    num_1 = input('Введите первое число: ').replace(' ', '').lower()
    num_2 = input('Введите второе число: ').replace(' ', '').lower()
    numbers_list.append(num_1)
    numbers_list.append(num_2)
    return numbers_list

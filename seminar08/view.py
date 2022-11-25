def action():
    action_lisr = [1, 2, 3, 4]
    ask_action = int(input('1 - Поиск контакта\n2 - Добавление контакта\n3 - Удаление контакта\n'
                           '4 - Редактирование контакта\nВыберите действие: '))
    while True:
        if ask_action in action_lisr:
            break
    return ask_action

from datetime import datetime

action_dict = {1: 'Поиск контакта',
               2: 'Добавление контакта',
               3: 'Удаление контакта',
               4: 'Редактирование контакта'
}


def logger(action):
    with open('log.txt', 'w', encoding='utf-8') as file:
        file.write('{curr_time}\t{action}\n'.format(
            curr_time=datetime.now(),
            action=action_dict.get(action),
        ))

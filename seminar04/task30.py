# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt.
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

my_dict = {}

with open('users.txt', 'r', encoding='utf-8') as users:
    user_list = users.read().split('\n')

with open('hobby.txt', 'r', encoding='utf-8') as hobby:
    hobby_list = hobby.read().split('\n')

for index in range(len(user_list)):
    my_dict[user_list[index]] = hobby_list[index]

with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobby:
    for key, value in my_dict.items():
        users_hobby.write('{}: {}\n'.format(key, value))

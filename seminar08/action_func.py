import csv


def add_contact():
    contact_dict = dict()
    max_id = 0
    data_info = {
        'name': 'имя',
        'surname': 'фамилию',
        'phone_number': 'номер телефона'
    }

    for graph in data_info:
        contact_dict[graph] = input('Введите {}: '.format(data_info.get(graph)))

    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            if int(row['id']) > max_id:
                max_id = int(row['id'])

    if max_id == 0:
        format_recording = 'w'
    else:
        format_recording = 'a'
    with open('contacts.csv', format_recording, encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'name', 'surname', 'phone_number']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if max_id == 0:
            csv_writer.writeheader()

        info_dict = {'id': f'{max_id + 1}'}
        info_dict.update(contact_dict)

        csv_writer.writerow(info_dict)

    print('Контакт добавлен')


def delete_contact():
    if search_contact():
        test_list = []
        id_contact = input('Введите ID контакт который хотите удалить: ')

        with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if row['id'] != id_contact:
                    test_list.append(row)

        with open('contacts.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'name', 'surname', 'phone_number']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for i in test_list:
                csv_writer.writerow(i)

    print('Контакт удален')


def edit_contact():
    if search_contact():
        test_list = []
        id_contact = input('Введите ID контакт который хотите изменить: ')

        with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if row['id'] != id_contact:
                    test_list.append(row)
                else:
                    row['name'] = input("Введите имя")
                    row['surname'] = input("Введите фамилию")
                    row['phone_number'] = input("Введите телефон")
                    test_list.append(row)

        with open('contacts.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'name', 'surname', 'phone_number']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for i in test_list:
                csv_writer.writerow(i)

    print('Контакт изменен')


def search_contact():
    contact_info = input('Введите данные для поиска: ').lower()
    flag = False

    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            all_string = ''
            for i in row:
                all_string += row[i]
            if contact_info in all_string.lower():
                flag = True
                print('Найдено контактов: ')
                print(row.get('id'), row.get('name'), row.get('surname'), row.get('phone_number'))

    if not flag:
        print('Поиск не дал результат')
    return flag

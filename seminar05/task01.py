# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) * Подумайте как наделить бота ""интеллектом""


import random


def take_candy(player):
    if player == 'Player':
        while True:
            candy = int(input('Сколько конфет берет Игрок? '))
            if 1 <= candy <= 28:
                break
            else:
                print('Введите число от 1 до 28.')
    else:
        candy = count_candy % 29
        if candy == 0:
            candy += 1
        print(f'Бот взял {candy} конфет!')
    return candy


count_candy = 2021


player_list = ['Player', 'Bot']
random.shuffle(player_list)

print('Начало игры!')
while True:
    count_candy -= take_candy(player_list[0])
    if count_candy <= 28:
        print('Выиграл:', player_list[1])
        break
    else:
        print('Осталось конфет: ', count_candy)
    count_candy -= take_candy(player_list[1])
    if count_candy <= 28:
        print('Выиграл:', player_list[0])
        break
    else:
        print('Осталось конфет:', count_candy)

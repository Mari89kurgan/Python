# 2. Создайте программу для игры в ""Крестики-нолики"".

def print_board():
    for i in range(len(board_list)):
        print(board_list[i], end=' ')
        if (i + 1) % 3 == 0:
            print()


def take_input(token, pole):
    while True:
        value = int(input(f'Куда поставить {token}? '))
        if not (value in pole):
            print('Ошибочный ввод. Повторите')
            continue
        pole[value - 1] = token
        break


def check_win(pole):
    for each in wins_coord:
        if pole[each[0] - 1] == pole[each[1] - 1] == pole[each[2] - 1]:
            return pole[each[0] - 1]
    else:
        return False


def main(pole):
    counter = 0
    while True:
        print_board()
        if counter % 2 == 0:
            take_input('Х', pole)
        else:
            take_input('O', pole)
        if counter > 3:
            winner = check_win(pole)
            if winner:
                print_board()
                print(winner, '- Выиграл')
                break
        counter += 1
        if counter > 8:
            print_board()
            print('Ничья')
            break

board_list = [number for number in range(1, 10)]
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

main(board_list)

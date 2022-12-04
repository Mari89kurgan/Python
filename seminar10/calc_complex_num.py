def get_part(number_list):
    number_list_part = list()
    for num in number_list:
        valid_part = ''
        imaginary_part = ''
        flag = True
        for i in range(len(num)):
            if flag:
                valid_part += num[i]
                if i == len(num) - 1:
                    break
                if num[i].isdigit() and not num[i + 1].isdigit():
                    flag = False
            else:
                imaginary_part += num[i]
        number_list_part.append(int(valid_part))
        number_list_part.append(int(imaginary_part[:-1:]))

    return number_list_part


def addition(number_list_part):
    a1 = number_list_part[0]
    b1 = number_list_part[1]
    a2 = number_list_part[2]
    b2 = number_list_part[3]
    sign = '+'
    if b1 + b2 < 0:
        sign = '-'
    return f'{a1 + a2}{sign}{abs(b1 + b2)}i'


def subtraction(number_list_part):
    a1 = number_list_part[0]
    b1 = number_list_part[1]
    a2 = number_list_part[2]
    b2 = number_list_part[3]
    sign = '+'
    if b1 - b2 < 0:
        sign = '-'
    return f'{a1 - a2}{sign}{abs(b1 - b2)}i'


def multiplication(number_list_part):
    a1 = number_list_part[0]
    b1 = number_list_part[1]
    a2 = number_list_part[2]
    b2 = number_list_part[3]
    sign = '+'
    if a1 * b2 + b1 * a2 < 0:
        sign = '-'
    return f'{a1 * a2 - b1 * b2}{sign}{abs(a1 * b2 + b1 * a2)}i'


def division(number_list_part):
    a1 = number_list_part[0]
    b1 = number_list_part[1]
    a2 = number_list_part[2]
    b2 = number_list_part[3]
    sign = '+'
    if (a1 * b2 + b1 * a2) / (a2 ** 2 + b2 ** 2) < 0:
        sign = '-'
    return f'{(a1 * a2 - b1 * b2) / (a2 ** 2 + b2 ** 2)}{sign}{abs((a1 * b2 + b1 * a2) / (a2 ** 2 + b2 ** 2))}i'

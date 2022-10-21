# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def fibonachi(number):
    fib1 = 1
    fib2 = 1
    fib_list = [fib1, fib2]
    i = 2
    while i < number:
        fib_sum = fib1 + fib2
        fib_list.append(fib_sum)
        fib1 = fib2
        fib2 = fib_sum
        i += + 1
    return fib_list


def n_fibonachi(number):
    fib1 = 1
    fib2 = -1
    n_fib_list = [fib1, fib2]
    i = 2
    while i < number:
        fib_dif = fib1 - fib2
        n_fib_list.append(fib_dif)
        fib1 = fib2
        fib2 = fib_dif
        i += + 1
    return list(reversed(n_fib_list))


print(n_fibonachi(8) + [0] + fibonachi(8))

# Задача №5 Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка

from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


print(f"{[el for el in range(99, 1001) if el % 2 == 0]}")
print(f"{reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}")

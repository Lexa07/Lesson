"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список
    должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления
    произведения всех элементов списка.
    Подсказка: использовать функцию reduce()."""


from random import randint
from functools import reduce

user = int(input("Список из какого количества чисел создать: "))
my_list = [randint(100, 1000) for i in range(user)]
new_list = [i for i in my_list if i % 2 == 0]


def func_my(el_1, el_2):
    return el_1 * el_2


multiplication = reduce(func_my, new_list)
print(f"Сформировали список: {my_list}")
print(f"Перемножив чётный список {new_list} получаем число: {multiplication}")

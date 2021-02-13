"""
    3. Создать текстовый файл (не программно), построчно записать фамилии
    сотрудников и величину их окладов. Определить, кто из сотрудников
    имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""
from functools import reduce


def func_my(el_1, el_2):
    return float(el_1) + float(el_2)


with open("text_3.txt", "r") as mytext:
    my_list = []
    zp = 20000  # вывел чтобы легче было менять ориентир по зарплате
    for line in mytext:
        worker = line.split(' ')
        my_list.append(worker[1])
        if float(worker[1]) < zp:
            print(worker[0])

    i = len(my_list)
    mnog = reduce(func_my, my_list)
    print(f"Средняя заработная плата сотрудников: {mnog / i} рублей.")

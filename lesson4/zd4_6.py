"""6. Реализовать два небольших скрипта:
    • итератор, генерирующий целые числа, начиная с указанного;
    • итератор, повторяющий элементы некоторого списка, определённого заранее.
    Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
    создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
    Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
    """
from itertools import count, cycle
from sys import argv

try:
    name, s_1, s_2 = argv
    my_list = []
    for el in count(int(s_1)):
        if el > int(s_2):
            print(my_list)
            break
        else:
            my_list.append(el)
    c = 0
    for el in cycle(my_list):
        if c > 10:
            break
        print(el)
        c += 1
except ValueError:
    print("Вы не ввели все данные, через пробел  zd4_6.py 'число начала списка' 'число окончания списка'. Попробуйте заново!")










"""5. Создать (программно) текстовый файл, записать в него
    программно набор чисел, разделенных пробелами. Программа
    должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("number.txt", "a") as mfile:
    while True:
        number = input('Введите числа, разделённые пробелами: ')
        if number != 'нет':
            print(number, file=mfile)
        else:
            break

with open("number.txt", "r", encoding='utf-8') as myfile:
    my_list = []
    for line in myfile:
        tex = line.replace('\n', '')
        text = tex.split(' ')
        for i in text:
            if i != '':
                a = int(i)
                my_list.append(a)
            else:
                print(i)
    num = sum(my_list)
    print("Сумма чисел в файле:   ", num)

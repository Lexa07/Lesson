"""1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
    проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""
my_list = [13, False, "Hello", -45, 2.14, [1, 2], (1, 2)]
for i in range(len(my_list)):
    print(type(my_list[i]))
print("Вроде так!")

for i, item in enumerate(my_list, 1):
    print(f"{i}{item} - {type(i)}")
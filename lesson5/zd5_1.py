"""
    1. Создать программно файл в текстовом формате, записать в него
    построчно данные, вводимые пользователем. Об окончании ввода
    данных свидетельствует пустая строка.
"""

with open("user.txt", "w", encoding="utf-8") as text:
    while True:
        user = input("Введите данные:  ")
        if user != "=":
            text.writelines(f"{user}\n")
        else:
            break






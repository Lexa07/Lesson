def deln(a, b):
    return a / b


while True:
    try:
        user1 = int(input('Введите делимое число: '))
        user2 = int(input('Введите делитель: '))
        print('%.2f' % (deln(user1, user2)))
        break
    except ZeroDivisionError:
        print("Введите пожалуйста числа ещё раз. Деление на ноль запрещено.")

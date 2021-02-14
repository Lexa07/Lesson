"""
    2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
    работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
    должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class Zer_m:
    def __init__(self, divisble, divisor):
        self.dvsbl = divisble
        self.dvsr = divisor

    def __del__(self):
        try:
            return f'деление: {(self.dvsbl // self.dvsr)}'
        except ZeroDivisionError:
            return "Деление на ноль запрещено!"


number_1 = int(input("Введите делимое число: "))
number_2 = int(input("Введите делитель: "))

delay = Zer_m(number_1, number_2)
print(delay.__del__())
"""
    1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
    формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
    должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
    @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def get_dat(cls, dat):
        my_list = []
        d = int(one.dat[:2])
        m = int(one.dat[3:5])
        y = int(one.dat[6:])
        my_list.append(d)
        my_list.append(m)
        my_list.append(y)
        return my_list

    @staticmethod  # что то не так с этим методом....
    def number_dat(self):
        if 0 > self[0] > 31:
            print("Не правильно введён день.")
        if 0 > self[1] > 13:
            print('Не правильно введён месяц')
        if 1000 > self[2] > 2200:
            print("Не правильно введён год")

        return f'{self[0]}-день {self[1]}-месяц {self[2]}-год'



da = "12-04-2021"
one = Data(da)
print(Data.get_dat(one))
print(Data.number_dat(Data.get_dat(one)))


"""
    2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
    название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
    одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
    быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
    (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
    знания: реализовать абстрактные классы для основных классов проекта, проверить на
    практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
   def __init__(self):
       pass

   @property
   @abstractmethod

   def rashet(self):
       pass

   def __add__(self, other):
       return self.rashet + other.rashet

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print("На детей не шьём. Начинаем с сорокового. Посчитаем для 40")
            self.__size = 40
        elif size > 58:
            print("Слишком большой размер. Максимум 58. Для 58 и произведём расчёт.")
            self.__size = 58
        else:
            self.__size = size

    @property
    def rashet(self):
        return self.__size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print("Слишком маленький размер. 100 минимум на него и посчитаем")
            self.__height = 100
        elif height > 240:
            print("Слишком большой. Максимум 240. Посчитаем на него.")
            self.__height = 240
        else:
            self.__height = height
    @property
    def rashet(self):
        return 2 * (self.__height / 100) + 0.3

coat_1 = Coat(int(input("Введите размер пальто для расчёта: ")))
print(f"Вам потребуется {coat_1.rashet:.2f} метров ткани на пальто {coat_1.size} размера")

costume_1 = Costume(int(input("Введите рост для костюма для рассчёта в сантиметрах: ")))
print(f"Вам потребуется {costume_1.rashet:.2f} метров ткани на пальто {costume_1.height} размера")
print(f"Всего Вам потребуется ткани {coat_1 + costume_1:.2f} метров")

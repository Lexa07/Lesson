"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
    (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из
    классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
    уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
    каждого экземпляра."""


class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f"Чтото написано")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen")

class Pencil(Stationery):
    def draw(self):
        print(f"Start draw with {self.title} pencil!")

class Handle(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} handle!")

stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
handle = Handle("Copic")
handle.draw()























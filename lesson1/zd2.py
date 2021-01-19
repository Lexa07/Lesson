"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
    выведите в формате чч:мм:сс. Используйте форматирование строк."""

user = int(input("Введите время в секундах "))

clock = int(user / 3600)
minutes = int((user - (3600 * clock)) / 60)
seconds = int(user - (clock * 3600 + minutes * 60))

print("Время {:02d}:{:02d}:{:02d}".format(clock, minutes, seconds))

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
    относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

m_list = ["Январь-зима",
          "Февраль-зима",
          "Март-весна",
          "Апрель-весна",
          "Май-весна",
          "Июнь-лето",
          "Июль-лето",
          "Август-лето",
          "Сентябрь-осень",
          "Октябрь-осень",
          "Ноябрь-осень",
          "Декабрь-зима"]

my_dict = {1: "Январь-зима",
           2: "Февраль-зима",
           3: "Март-весна",
           4: "Апрель-весна",
           5: "Май-весна",
           6: "Июнь-лето",
           7: "Июль-лето",
           8: "Август-лето",
           9: "Сентябрь-осень",
           10: "Октябрь-осень",
           11: "Ноябрь-осень",
           12: "Декабрь-зима"}

while True:
    try:
        user = int(input("Введите номер месяца года: "))
        if user <= 0:
            user = 33
        print(m_list[user - 1])
        print(my_dict.get(user))
    except IndexError:
        print("Вы ввели не правильно. Попробуйте ещё...")
    except ValueError:
        print("Вы ввели не правильно. Попробуйте ещё...")
    else:
        break

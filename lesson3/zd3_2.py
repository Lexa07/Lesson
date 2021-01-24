

def user(**kwargs):
    return print(kwargs)

name = input("Введите имя: ")
firstname = input("Введите фамилию: ")
age = input("Введите возраст: ")
city = input("Введите город проживания: ")
email = input("Введите эл.адрес: ")
tel = input("Введите телефон: ")

user(name={name}, firstname={firstname}, age={age}, city={city}, email={email}, tel={tel})

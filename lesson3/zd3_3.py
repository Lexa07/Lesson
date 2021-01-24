
def my_func(a, b, c):
    if a < b > c:
        print(b)
    elif b < a > c:
        print(a)
    else:
        print(c)
    return


a = input("Введите 1-е число: ")
b = input("Введите 2-е число: ")
c = input("Введите 3-е число: ")

my_func(a, b, c)
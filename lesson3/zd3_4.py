
def my_func(x, y):
    s = x ** y
    print(s)

my_func(2,-5)



# ИЛИ ТАК :


def m_func(x, y):
    c = 1
    while y != 0:
        c = 1 / x * c
        y += 1
    print('%.5f' % (c))

m_func(2, -5)



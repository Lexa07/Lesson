

def summa(*args):
    for n in args:
        print(sum(n))
    return


a = []


while True:
    try:
        my_list = input("Введите строку чисел, разделённых пробелом, для выхода введите любую букву: ").split()
        for i in my_list:
            c = int(i)
            a.append(c)
    except ValueError:
        summa(a)
        break
    else:
        summa(a)


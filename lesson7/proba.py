mlist = [1, 2, 3, 4, 5, 6]
for i in range(len(mlist))
    b = "a_" + str(i)
    print(b, mlist[i])






my_list = [[78, 67], [65, 87, 1355], [31, 21], [99, 22]]
list_my = [[89], [98, 90], [77, 81], [45, 35]]
number = []
s = []
d = []
for i in range(len(my_list)):
    a = my_list[i]
    b = list_my[i]
    if len(a) > len(b):
        for t in range(len(a) - len(b)):
            b.append(0)
    else:
        for r in range(len(b) - len(a)):
            a.append(0)

    for el in range(len(a)):
        num = a[el] + b[el]
        number.append(num)
print(number)



from random import randint
def rand(cic):
    number = []
    for i in range(cic):
        number.append(randint(1, 1000))
        i += 1
    return number



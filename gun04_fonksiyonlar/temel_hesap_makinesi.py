def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    if y == 0:
        print("Tanimsiz !!!")
        return None
    return x / y


print(toplama(10, 20))
print(cikarma(20, 10))
print(carpma(6, 8))
print(bolme(60, 12))
print(bolme(8, 0))

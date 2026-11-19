def buyuk(a, b, c, en_buyuk=0):
    en_buyuk = a

    if c > en_buyuk and c > b:
        return c
    elif b > en_buyuk and b > c:
        return b
    return a


print(buyuk(2, 1, 3))

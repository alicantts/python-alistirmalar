def asal(sayi):

    if sayi > 1:
        for i in range(2, sayi):
            if sayi % i == 0:
                bayrak += 1

        bayrak = 0
        if bayrak > 0:
            return False
        else:
            return True
    else:
        return False


print(asal(int(input("Sayi asal mi: "))))

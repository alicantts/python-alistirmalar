def rakamlar_toplami(sayi):
    toplam = 0
    if sayi == 0:
        return None
    else:
        while sayi != 0:
            kalan = sayi % 10
            bolum = sayi // 10
            sayi = bolum
            toplam += kalan

        return toplam


sayi = int(input("Sayi giriniz: "))
print(rakamlar_toplami(sayi))

#finish
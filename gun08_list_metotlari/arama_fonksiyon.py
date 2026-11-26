notlar = [10, 20, 30, 20, 40, 80, 10, 100, 75, 90, 30, 50, 60, 95]


def arama(puan):

    aranan = []

    for i in range(len(notlar)):
        if notlar[i] == puan:
            aranan.append(i)

    if puan in notlar:
        return print(
            "\nNot alinmis!",
            "\nNotu alan ogrencilerin sirasi: ",
            aranan,
            f"\n{puan} notunu alan kisi sayisi: ",
            notlar.count(puan),
        )

    else:
        return f"{puan} alan ogrenci bulunmamaktadir!!!"


puan = int(input("Aradiginiz notu giriniz: "))

arama(puan)

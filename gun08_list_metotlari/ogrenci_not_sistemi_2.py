notlar = []


def not_ekle(notlar):
    while True:
        puan = int(input("Not Giriniz: "))
        if 0 <= puan <= 100:
            notlar.append(puan)
            return f"\nYeni puan listesi: {notlar}"
        else:
            print("Gecerli bir not giriniz !!!")


def not_sil(notlar):
    if len(notlar) == 0:
        return "Liste bos !!!"

    while True:

        sil = int(input("Silinecek notu giriniz: "))
        if sil in notlar:
            notlar.remove(sil)
            return f"\n Yeni liste: {notlar}"

        else:
            print("Gecerli bir not giriniz !!!")


def son_not_sil(notlar):
    if len(notlar) > 0:
        silinen = notlar.pop()
        return f"Silinen not: {silinen}\n" f"Güncel Liste: {notlar}"
    else:
        return "Bos liste !!!"


def kucuk_buyuk(notlar):
    if len(notlar) == 0:
        return "Bos liste !!! "
    else:
        notlar.sort()
        return f"Kucukten buyuge siralanmis liste: {notlar}"


def buyuk_kucuk(notlar):
    if len(notlar) == 0:
        return "Bos liste !!! "
    else:
        return f"Buyukten kucuge siralanmis liste: {sorted(notlar,reverse=True)}"


def ortalama(notlar):
    if len(notlar) == 0:
        return "Ortalama: 0 (Bos liste)"
    else:
        toplam = 0
        for i in notlar:
            toplam += i
        sonuc = toplam / (len(notlar))
        return f"Not ortalamasi: {sonuc}"


def temizle(notlar):
    if len(notlar) == 0:
        return "Liste zaten bos !!!"
    else:
        notlar.clear()
        return "Notlar temizlendi."


def cikis(notlar):
    return "Programdan cikiliyor..."


while True:

    print("\n--- NOT SISTEMI ---")
    print("1 - Not ekle")
    print("2 - Not sil")
    print("3 - Son notu sil")
    print("4 - Kucukten buyuge sirala")
    print("5 - Buyukten kucuge sirala")
    print("6 - Not ortalamasi")
    print("7 - Butun notlari sil")
    print("8 - Cikis")

    secim = int(input("Seciminiz: "))

    if secim == 1:
        print(not_ekle(notlar))

    elif secim == 2:
        print(not_sil(notlar))

    elif secim == 3:
        print(son_not_sil(notlar))

    elif secim == 4:
        print(kucuk_buyuk(notlar))

    elif secim == 5:
        print(buyuk_kucuk(notlar))

    elif secim == 6:
        print(ortalama(notlar))

    elif secim == 7:
        print(temizle(notlar))

    elif secim == 8:
        print(cikis())
        break

    else:
        print("Gecersiz secim!")

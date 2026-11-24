from gün07_mini_sınav.soru1 import ortalama

while True:
    n = int(input("Kaç adet not girilecek?: "))
    adet = n
    toplam = 0
    if n == 0:
        print("Adet 0 girildigi icin not alinmadi. Ortalama hesaplanmadi.")
        print(ortalama(toplam, adet))

    else:
        if n < 0:
            print(ortalama(toplam, adet))
        else:
            while n > 0:
                nt = float(input("not giriniz: "))
                if nt < 0 or nt > 100:
                    print("Gecerli not girmek için yeniden deneyiniz !!!")
                    continue
                n -= 1
                toplam += nt

            print(ortalama(toplam, adet))

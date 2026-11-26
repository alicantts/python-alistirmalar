def sira(notlar):

    while True:

        secim = int(
            input(
                "Siralama secimi (1.Bastan sona , 2.Sondan Basa , 3.Girilme sirasi ile):"
            )
        )
        if secim == 1:
            bastan_sona = sorted(notlar)
            return bastan_sona
        elif secim == 2:
            return sorted(notlar, reverse=True)
        elif secim == 3:
            return notlar
        else:
            print("Gecerli bir islem giriniz !!!")


def gec_kal(notlar):
    gecenler = [puanlar for puanlar in notlar if puanlar >= 60]
    kalanlar = [puanlar for puanlar in notlar if puanlar < 60]
    return (f"{gecenler} alan(lar) gecti.", f"{kalanlar} alan(lar) kaldi.")


notlar = []
puan = 0
i = 1

while True:
    a = int(input("Kac not girilecek? :"))
    if a <= 0:
        print("Gecerli bir deger Giriniz !!!")
    else:
        break

while i <= a:
    puan = 0
    puan = float(input(f"{i}. notu giriniz: "))
    if 0 <= puan <= 100:
        notlar.append(puan)
        i += 1
    else:
        print("Gecerli bir puan giriniz !!!")
        continue

print(sira(notlar))
print(gec_kal(notlar))

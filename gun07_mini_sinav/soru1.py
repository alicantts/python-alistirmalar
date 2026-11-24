def ortalama(toplam, adet):

    if adet < 0:
        return "Adet negatif girildiği için ortalama hesaplanmadi."
    elif adet == 0:
        return None

    ort = toplam / adet
    if 90 <= ort <= 100:
        return f"Ortalama: {ort}. Harf notu: 'A'. \n"
    elif 80 <= ort < 90:
        return f"Ortalama: {ort}. Harf notu: 'B'. \n"
    elif 70 <= ort < 80:
        return f"Ortalama: {ort}. Harf notu: 'C'. \n"
    elif 60 <= ort < 70:
        return f"Ortalama: {ort}. Harf notu: 'D'. \n"
    elif 0 < ort < 60:
        return f"Ortalama: {ort}. Harf notu: 'F'. \n"


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

        #finish
        

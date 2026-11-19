sayi = 1
toplam = 0
sayac = 0

while(sayi != 0):
    sayi = int(input("Sayi giriniz: "))
    if(sayi == 0):
        break;

    toplam+=sayi
    sayac+=1

print(f"Simdiye kadar girilen '0 haric' {sayac} sayinin toplami {toplam}'dir.")


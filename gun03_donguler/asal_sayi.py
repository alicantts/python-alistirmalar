sayi = int(input("Sayi giriniz: "))
bayrak = 0

if sayi>1:
    for i in range (2,sayi):
        if (sayi%i == 0):
         bayrak  += 1

    if (bayrak>0):
     print(f"{sayi} sayisi asal degildir.")
    else:print(f"{sayi} sayisi asaldir.")
else: print("Asalligi incelenebilir sayi giriniz !!!")



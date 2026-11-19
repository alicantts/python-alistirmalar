sayi = int(input("Sayi giriniz: "))
fak = 1

if (sayi>=0):
    for sayi in range(sayi,0,-1):
     fak*=sayi
    print(f"Sayinin faktoriyeli:{fak}'dir")
else:print("Hatali sayi girdiniz !!!")


sayi = int(input("Sayi giriniz: "))

if (sayi<0):
    print("Hatali sayi girdiniz !!!")
else:
 fak = 1
 while(sayi>0):

    fak*=sayi
    sayi-=1
 print(f"Sayinin faktoriyeli:{fak}'dir")

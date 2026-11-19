n = int(input("Sayi giriniz: "))

if(0<=n<=20):
    for i in range(0,n):
        print(pow(i,2))
else:print("Hatali giris !!! (0<= n <= 20)")

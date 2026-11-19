def faktoriyel(x):
    fak = 1
    if x >= 0:
        for sayi in range(x, 0, -1):
            fak *= sayi
        return f"Sayinin faktoriyeli:{fak}'dir"
    else:
        return None


print(faktoriyel(int(input("Sayi giriniz: "))))

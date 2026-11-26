# sayilar = [34, 67, 90, 23, 46]

# buyukler = []
# kucukler = []

# for sayi in sayilar:
#     if sayi >= 20:
#         buyukler.append(sayi)

# print(buyukler)


# for sayi in sayilar:
#     if sayi <= 20:
#         kucukler.append(sayi)

# print(kucukler)


# sayilar = [15, 60, 35, 80, 20, 95, 45]


# def yirmiden_buyuk(sayilar):
#     return sayilar >= 20


# sonuc = filter(yirmiden_buyuk, sayilar)

# print(list(sonuc))
#  [60, 35, 80, 20, 95, 45]


# sayilar = [10, 45, 20, 75, 30, 90, 15, 55]

# sonuc = filter(lambda sayi: sayi > 30, sayilar)

# print(list(sonuc))


sayilar = [12, 7, 25, 40, 33, 18, 51, 60]

kucukler = [sayi for sayi in sayilar if sayi % 2 != 0]

print(kucukler)

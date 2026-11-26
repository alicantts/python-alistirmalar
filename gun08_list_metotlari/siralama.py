sayilar = [45, 12, 78, 23, 9, 56, 34]

# 1. Ters çevirme
sayilar.reverse()
print(sayilar)

# 2. Orijinali bozmadan sıralama
yeni_liste = sorted(sayilar)
print(yeni_liste)

# 3. Küçükten büyüğe
sayilar.sort()
print(sayilar)


# 4. Büyükten küçüğe
sayilar.sort(reverse=True)
print(sayilar)

notlar = [45, 70, 85, 60, 90, 70, 35, 100]

print(85 in notlar)
# true
print(50 in notlar)
# false

print(notlar.index(70))
# 1

# print(notlar.index(0))
# Traceback (most recent call last):
#   File "c:\dev\python-alisirmalar\gun08_list_metotlari\arama.py", line 7, in <module>
#     print(notlar.index(0))
#           ~~~~~~~~~~~~^^^
# ValueError: list.index(x): x not in list

print(notlar.count(70))
# 2

print(notlar.index(70, 2))
# 5


####
print(notlar.index(70, 2, 7))
# 5

print(notlar.index(70, 2, 7))
# 1

# örnek arama programi
if 101 in notlar:
    print(notlar.index(101))
else:
    print("Aradiginiz eleman listede bulunamadi")
# Aradiginiz eleman listede bulunamadi

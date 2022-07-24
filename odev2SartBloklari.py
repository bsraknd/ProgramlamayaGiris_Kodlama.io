# sayilar = []
# print("Birinci Sayıyı giriniz :")
# a = input()
# sayilar.append(a)
# print("İkinci Sayıyı giriniz :")
# b = input()
# sayilar.append(b)
# print("Üçüncü Sayıyı giriniz :")
# c = input()
# sayilar.append(c)
# print(max(sayilar))

print("Birinci Sayıyı giriniz :")
a = input()

print("İkinci Sayıyı giriniz :")
b = input()

print("Üçüncü Sayıyı giriniz :")
c = input()

if a > b and a > c:
    if (b > c):
        print("En Küçük Sayı:" + c)
    else:
        print("En Küçük Sayı:" + b)
    print("En Büyük Sayı :" + a)
elif c > a and c > b:
    if (a > b):
        print("En Küçük Sayı:" + b)
    else:
        print("En Küçük Sayı:" + a)
    print("En Büyük Sayı :" + c)
else:
    if (c > a):
        print("En Küçük Sayı:" + a)
    else:
        print("En Küçük Sayı:" + c)
    print("En Büyük Sayı:" + b)
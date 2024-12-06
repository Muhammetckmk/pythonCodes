names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)
# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)
# 3-  "Deniz" ismini listeden siliniz.
#names.remove("Deniz")
print(names)
# 4-  "Deniz" isminin indeksi nedir ?
a=names.index("Deniz")
print(a)
# 5-  "Ali" listenin bir elemanı mıdır ?
if 'Ali' in names:
    print("listede vardır")
else:
    print("listede yoktur")

# result = 'Ali' in names
# result = names.index('Ali')

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
years.reverse()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
k=str.split(',')
print(k)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
m=min(years)
n=max(years)
print(m)
print(n)
# 11- years dizisinde kaç tane 1998 değeri vardır ?
z=years.count(1998)
print(z)
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka=[]
print(marka.append(input("bir marka giriniz : ")))
print(marka.append(input("bir marka giriniz : ")))
print(marka.append(input("bir marka giriniz : ")))

print(marka)


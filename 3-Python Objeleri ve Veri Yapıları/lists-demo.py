# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars=['Bmw', 'Mercedes','Opel','Mazda']
print(cars)
# 2-  Liste Kaç elemanlıdır ?
print(len(cars))

# 3-  Listenin ilk ve son elemanı nedir ?
print(cars[0])
print(cars[-1])
# 4-  Mazda değerini Toyota ile değiştirin.
cars[cars.index('Mazda')]='Toyota'
print(cars)
# 5-  Mercedes listenin bir elemanı mıdır ?
a= 'Mercedes' in cars
print(a)
# 6-  Listenin -2 indeksindeki değer nedir ?
b=cars[-2]
print(b)
# 7-  Listenin ilk 3 elemanını alın.
print(cars[:3])

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
print(cars[-2:])

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
cars.append('Audi')
cars.append('Nissan')
print(cars)
# 10- Listenin son elemanını silin.
cars.pop(-1)
print(cars)
# 11- Liste elemanlarını tersten yazdırınız.
cars.reverse()
print(cars)
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 
# studentA: Muhammet Çakmak 1992, (70,60,70)
# studentB: Nimet Çakmak  1993, (80,80,70)
# studentC: Musab Fatih Çakmak 2025, (80,70,90)

studentA = ['Muhammet','Çakmak',1992,[70,60,70]]
studentB = ['Nimet','Çakmak',1993,[80,80,70]]
studentC = ['Musab Fatih','Çakmak',2025,[80,70,90]]

result = studentA[0]
print(result)
result = studentB[1]
print(result)
result = studentC[3][1]
print(result)

result = f"{studentA[0]} {studentA[1]} {2024-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)

# 13- Liste elemanlarını ekrana yazdırınız.




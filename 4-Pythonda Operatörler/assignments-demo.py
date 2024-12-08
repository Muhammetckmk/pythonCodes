x, y, z = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a=int(input("bir sayı giriniz : "))
b=int(input("bir sayı giriniz : "))
z=(a*b)-(x+y+z)
print(z)
a = int(input('1.sayı: '))
b = int(input('2.sayı: '))

result = (a * b) - (x+y+z)

# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
m=int(y/x)
print("m: ",m)


# 3- (x,y,z) toplamının mod 3' ü nedir ?
print((x+y+z)%3)



# 4- y' nin x. kuvvetini hesaplayınız.
print(y**x)

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?



# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
result = y ** x

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y ,z = numbers
print(x,y,z)

result1 = z ** 3
print(result1)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?

numbers = 1, 5, 7, 10, 6
x, *y ,z = numbers

result2 = y[0] + y[1] + y[2]

print(result2)


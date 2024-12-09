
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.



# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#sayi=int(input('Bir sayı giriniz : '))
#soru=sayi>0 and sayi%2==0
#print(soru)

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
email='muhammetckmk46@gmail.com'
sifre=123456

print(email=='muhammetckmk46@gmail.com' and sifre==123456)


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

#a = int(input('a: '))
#b = int(input('b: '))
#c = int(input('c: '))
#
#result = (a > b) and  (a > c)
#print(f'a en büyük sayıdır : {result}')
#
#result = (b > a) and (b > c)
#print(f'b en büyük sayıdır : {result}')
#
#result = (c > a) and (c > b)
#print(f'c en büyük sayıdır : {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

#vize1=int(input('birinci vize notunuz : '))
#vize2=int(input('ikinci vize notunuz : '))
#final=int(input('final notunuz : '))
#ortalama=(vize1*30/100)+(vize2*30/100)+(final*40/100)
#print(ortalama)
# print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')




# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name=input("adınızı : ")
boy= float(input("boyunuz : "))
kilo= float(input("kilonuz : "))

indx=kilo/(boy**2)
zayıf=indx<=18.4
normal=(indx>18.4) and (indx<=24.9)
kilolu=(indx>24.9) and (indx<=29.9)
obez=indx>29.9
print(f'sayın {name}: kilo ve boy oranınız alındığında siz zayıf :{zayıf} sınız')
print(f'sayın {name}: kilo ve boy oranınız alındığında siz normal:  {normal} sınız')
print(f'sayın {name}: kilo ve boy oranınız alındığında siz kilolu: {kilolu} sınız')
print(f'sayın {name}: kilo ve boy oranınız alındığında siz obez : {obez} sınız')







name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')



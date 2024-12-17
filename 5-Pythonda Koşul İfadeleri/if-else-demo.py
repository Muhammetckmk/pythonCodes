# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

#isim=str(input('isminiz giriniz: '))
#age=int(input('yaşınızı giriniz: '))
#egitim=str(input('eğitim durumunuzu giriniz: '))
#
#if age>=18:
#    if (egitim=='lise' or egitim=='üniversite'):
#        print(f'{isim } ehliyet alabilir')
#else:
#    print(f'{isim }ehliyet alamaz')



# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

note1= float(input('1. yazılı notunuzu giriniz :'))
note2= float(input('2. yazılı notunuzu giriniz :'))
sözlü= float(input('sözlü yazılı notunuzu giriniz :'))

ortalama=(note1+note2+sözlü)/3

if ortalama>0 and ortalama<24:
    print('notunuz 0 dır')
if ortalama>24 and ortalama<44:
    print('notunuz 1 dır')
if ortalama>45 and ortalama<54:
    print('notunuz 2 dır')
if ortalama>54 and ortalama<69:
    print('notunuz 3 dır')
if ortalama>69 and ortalama<84:
    print('notunuz 4 dır')
if ortalama>84 and ortalama<101:
    print('notunuz 5 dır')


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün
import datetime


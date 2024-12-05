"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""
musteriAdı ='Muhammet'
musteriSoyadı='Çakmak'
adSoyad=musteriAdı+' '+musteriSoyadı
cinsiyet='Erkek'
tcNo=12345678912
dogumyılı=1992
adres='Samsun'
yas=2024-dogumyılı

print(f"{adSoyad}\n {cinsiyet}\n {tcNo}\n {dogumyılı}\n {adres}\n {yas}")


"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total:", total)
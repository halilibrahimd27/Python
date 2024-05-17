#********anlıkTarihveSaat*********

import datetime

e = datetime.datetime.now()

print ("Güncel tarih ve saat = %s" %e)
print ("Bugünün tarihi:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("Saat: = %s:%s:%s" % (e.hour, e.minute, e.second))


#*********mukemmelsayı***********

sayi = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1

if (toplam == sayi):
    print(sayi,"mükemmel bir sayıdır.")
else:
    print(sayi,"mükemmel bir sayı değildir.")
    
    
#********armstrongsayı********
sayi = input("Sayı:")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

gecici_sayi = sayi

while (gecici_sayi > 0):
    basamak = gecici_sayi % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayi //= 10

if (toplam == sayi):
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")


#********fibonacci********

a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)


#********kokBulma********

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci Kök: {}\nİkinci Kök: {}\n ".format(x1,x2))



#********kullaniciGiris********

sys_kulanci_adi = "ibo"

sys_parola = "27467344"

giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")

    if(kullanici_adi !=sys_kulanci_adi and parola == sys_parola):
        print("Kullanıcı adını hatalı girdiniz.")
        giris_hakki -= 1

    elif(kullanici_adi == sys_kulanci_adi and parola != sys_parola):
        print("Parolayı hatalı girdiniz.")
        giris_hakki -= 1

    elif(kullanici_adi !=sys_kulanci_adi and parola != sys_parola):
        print("Kullanıcı adını ve parolayı hatalı girdiniz.")
        giris_hakki -= 1

    else:
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
        break

    if(giris_hakki == 0):
        print("Daha sonra tekrar deneyiniz...")
        break
    
    
#********sayiOkunusYazma********
    
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci] + " " + birler[birinci]


sayi = int(input("Sayı:"))

print(okunus(sayi))



#********tamBolenler********


def tambolenleribulma(sayi):
    
    tam_bolenler = []

    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler

while True:

    sayi = input("Sayi:")

    if(sayi == "0"):
        print("Program sonlandırılıyor...")
        break

    else:
        sayi = int(sayi)
        print("Tam bölenler: ",tambolenleribulma(sayi))
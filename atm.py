import os

os.system("figlet ATM")

banner='''
Bakiyenizi Öğrenmek İçin :[1]
Bakiyenize Para Yatırmak İçin :[2]
Bakiyenizden Para Çekmek İçin :[3]
Uygulamadan Çıkmak İçin :[q]

'''
print(banner)
para = 2000
while True:
    islem = input("İslem Seciniz :")
    if (islem == 'q' or 'Q'):
        print("Atm'den cıkılıyor")
        break
    elif (islem == '1'):
        print(f"Bankanızda {para} TL bulunmaktadır.")
    elif(islem=='2'):
        yatir=int(input("Yatırmak istediğiniz tutar :"))
        para+=yatir
        print(f"Bakiyeniz {para}")
    elif(islem=='3'):
        cek=int(input("Çekmek istediğiniz tutar:"))
        para-=cek
        print(f"Bakiyeniz {para}")
    else:
        print("Hatalı seçim tekrar seçim yapınız.")

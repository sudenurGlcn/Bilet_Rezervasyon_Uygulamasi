import Rezervasyon
import YeniEtkinlik
import Tutar
secim=0
while(secim!=3):
    print("\n")
    secim=int(input("1-Rezarvasyon\n2-Salon Durum Bilgisi\n3-Yeni Etkinlik\n4-Toplam Ciro\n5-Cıkıs\nSeçiminiz:"))
    if secim==1:
         print("Rezervasyon Yapılıyor...")
         Rezervasyon.rezervasyonYap()
    elif secim==2:
        print("Salon Durum Bilgisi")
        Rezervasyon.salonDurumBilgisi()
    elif secim==3:
        print("Yeni Etkinlik")
        YeniEtkinlik.EtkinlikSifirla()
    elif secim==4:
        print("Toplam Ciro")
        Tutar.ToplamCiro()
    elif secim==5:
        #Burada kullanıcı çıkış yapmak istediğinde bilet.txt dosyasına hangi koltukların dolu ve boş olduğu  durumunu kaydediyoruz.
        f=open("bilet.txt","w")
        for i in range(0,20):
            for j in range(0,20):
                f.write(Rezervasyon.bilet[i][j])
            f.write("\n")
        f.close()
        print("Cıkıs")
        break
    else:
        print("Hatalı Giriş")
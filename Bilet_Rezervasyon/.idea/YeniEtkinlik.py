import Rezervasyon
import Tutar
#tüm değişkenler ve fonksiyonları en baştaki boş hale getiriyoruz

def EtkinlikSifirla():
    for i in range(0,20):
        for j in range(0,20):
            Rezervasyon.bilet[i][j]="-"
    for i in range(0,4):
        Rezervasyon.biletSayilari[i]=0
    f=open("bilet.txt","w")
    for i in range(0,20):
        for j in range(0,20):
            f.write(Rezervasyon.bilet[i][j])
        f.write("\n")
    f.close()
    f = open("ciro.txt", "w")
    for i in range(4):
        f.writelines(str(0))
        if i != 3:
            f.write("\n")
    f.close()
    print("Etkinlik Sıfırlandı")






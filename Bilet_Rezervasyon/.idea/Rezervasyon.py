from typing import List
import Tutar


bilet=[["-" for x in range(20)] for y in range(20)]
biletSayilari=[100,100,100,100]
bilet2=[[0 for x in range(20)] for y in range(20)]
#dizi=[]

#Bu fonksiyon koltukların boş veya dolu olup olmama durumunu kontrol ediyor. Boş ise kullanıcı için ayırıyor.
def rezervasyonYap():
    #bilet.txt dosyasından gerekli değerleri okuyoruz
    f=open("bilet.txt","r")
    c=0
    for i in f.readlines():
        bilet[c]=list(i.rstrip("\n"))
        c+=1
    f.close()
    kategori=int(input("Kategori Seçiniz:"))
    biletSayisi=int(input("Kaç bilet almak istiyorsunuz(1-"+str(Tutar.maxBilet)+"):"))
    temp=biletSayisi
    biletSayilari=[100,100,100,100]
    biletSayilari=biletsayisiguncelle(biletSayilari)
    if(kategori==1):
        if biletSayisi > biletSayilari[kategori - 1]:
            print("Yeterli bilet yok.. Lütfen başka kategori seçiniz!")
            rezervasyonYap()
        elif biletSayisi>Tutar.maxBilet:
            print("En fazla",Tutar.maxBilet,"bilet satın alabilirsiniz!")
            rezervasyonYap()
        else:
            koltuklar=""
            i=0
            j=5
            #bilet sayısı kadar döngüye giriyor ve kategoriye göre koltukları veriyoruz
            while(biletSayisi>0):
                if bilet[i][j]=="-":
                    biletSayilari[kategori-1]-=1
                    bilet[i][j]="X"
                    biletSayisi-=1
                    koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                if(j==14):
                     i=i+1
                     j=4
                j=j+1
            print("Koltuk Numaraları:"+koltuklar.rstrip(","))
            #biletlerin fiyatlandırmasını yapmak için kategori ve bilet sayısını tutar.py dosyasına gönderiyoruz
            Tutar.biletTutariniOku(kategori,temp)
            print(kategori,". kategori kalan bilet sayısı: ",biletSayilari[kategori-1],sep='')

    elif(kategori==2):
        if biletSayisi > biletSayilari[kategori - 1]:
            print("Yeterli bilet bulunmuyor.. Lütfen başka kategori seçiniz.")
            rezervasyonYap()
        elif biletSayisi>Tutar.maxBilet:
            print("En fazla",Tutar.maxBilet,"bilet satın alabilirsiniz")
            rezervasyonYap()
        else:
            koltuklar=""
            #ikinci kategorideki koltukların yerleri arasında boşluk olduğu için 2 farklı döngüye girdik
            for i in range(0,10):
                if '-' not in bilet[i][0:5] and '-' not in bilet[i][15:20]:
                    #taradığı satırda o kategoride boş koltuk yoksa alt satıra geçiyor
                    continue
                cikis=False
                for j in range(4,-1,-1):
                    if(bilet[i][j]=="-"):
                        biletSayilari[kategori - 1] -= 1
                        bilet[i][j] = "X"
                        biletSayisi -= 1
                        koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                    if biletSayisi<=0:
                        cikis=True
                        break
                if cikis:
                    break
                for j in range(15,20):
                    if(bilet[i][j]=="-"):
                        biletSayilari[kategori - 1] -= 1
                        bilet[i][j] = "X"
                        biletSayisi -= 1
                        koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                    if biletSayisi<=0:
                        cikis=True
                        break
                if cikis:
                    break
            print("Koltuk numaraları:"+koltuklar.rstrip(","))
            Tutar.biletTutariniOku(kategori,temp)
            print(kategori,". kategori kalan bilet sayısı: ",biletSayilari[kategori-1],sep='')
     #birinci kategoriyile tamamen aynı işlemleri yapıyoruz
    elif(kategori==3):
        if biletSayisi > biletSayilari[kategori - 1]:
            print("Yeterli bilet bulunmuyor.. Lütfen başka kategori seçiniz.")
            rezervasyonYap()
        elif biletSayisi>Tutar.maxBilet:
            print("En fazla",Tutar.maxBilet,"bilet satın alabilirsiniz")
            rezervasyonYap()
        else:
            koltuklar=""
            i=10
            j=5
            while(biletSayisi>0):
                if bilet[i][j]=="-":
                    biletSayilari[kategori-1]-=1
                    bilet[i][j]="X"
                    biletSayisi-=1
                    koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                if(j==14):
                    i=i+1
                    j=4
                j=j+1
            print("Koltuk numaraları:" + koltuklar.rstrip(","))
            Tutar.biletTutariniOku(kategori,temp)
            print(kategori,". kategori kalan bilet sayısı: ",biletSayilari[kategori-1],sep='')
    #2. kategorideki gibi yine iki farklı döngüye girdik
    elif(kategori==4):
        if biletSayisi > biletSayilari[kategori - 1]:
            print("Yeterli bilet bulunmuyor.. Lütfen başka kategori seçiniz.")
            rezervasyonYap()
        elif biletSayisi>Tutar.maxBilet:
            print("En fazla",Tutar.maxBilet,"bilet satın alabilirsiniz")
            rezervasyonYap()
        else:
            koltuklar=""
            for i in range(10,20):
                if '-' not in bilet[i][0:5] and '-' not in bilet[i][15:20]:
                    continue
                cikis=False
                for j in range(4,-1,-1):
                    if(bilet[i][j]=="-"):
                        biletSayilari[kategori - 1] -= 1
                        bilet[i][j] = "X"
                        biletSayisi -= 1
                        koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                    if biletSayisi<=0:
                        cikis=True
                        break
                if cikis:
                    break
                for j in range(15,20):
                    if(bilet[i][j]=="-"):
                        biletSayilari[kategori - 1] -= 1
                        bilet[i][j] = "X"
                        biletSayisi -= 1
                        koltuklar += str(i + 1) + "-" + str(j + 1) + ",";
                    if biletSayisi<=0:
                        cikis=True
                        break
                if cikis:
                    break
            print("Koltuk numaraları:"+koltuklar.rstrip(","))
            Tutar.biletTutariniOku(kategori,temp)
            print(kategori,". kategori kalan bilet sayısı: ",biletSayilari[kategori-1],sep='')
    dosyaguncelle(bilet)

#Salonun son halini yazdırmak için kullanılanıyoruz.
def salonDurumBilgisi():
    f=open("bilet.txt","r")
    for i in f.readlines():
        print(i.rstrip("\n"))
    f.close()

#Burda en son bilet sayılarında ve biletlerin yerlerindeki değişiklikleri güncelliyoruz
def dosyaguncelle(bilet):
    f=open("bilet.txt","w")
    for i in bilet:
        f.writelines(i)
        f.write("\n")
    f.close()

def biletsayisiguncelle(biletSayilari):
    for i in bilet[0:10]:
        biletSayilari[0]-=i[5:15].count('X')
        biletSayilari[1]-=i[0:5].count('X')+i[15:20].count('X')
    for i in bilet[10:20]:
        biletSayilari[2]-=i[5:15].count('X')
        biletSayilari[3]-=i[0:5].count('X')+i[15:20].count('X')
    return biletSayilari
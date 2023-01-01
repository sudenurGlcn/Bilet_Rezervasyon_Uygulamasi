toplamTutar=[None for x in range(4)]
c=0
#bilet tutarlarını kategoriye göre ciro değerlerine eklemek ve saklamak için ciro dosyasını okuyoruz
with open('ciro.txt', 'r') as f:
    for i in f.readlines():
        toplamTutar[c]=float(i.rstrip("\n"))
        c+=1
with open('indirim.txt', 'r') as f:
    lines = f.readlines()
maxBilet = int(lines[0][2:])

def biletTutariniOku(kategori, ticket_count):

    # gerekli değişkenleri tanımlıyoruz
    fiyat = []
    indirimler = []
    # bilet fiyatlarını ve indirimleri saklıyoruz
    for line in lines[1:5]:
        fiyat.append(int(line[2:]))
    for line in lines[5:]:
        if line[0] == 'M':
            pass
        else:
            split_line = line.split('-')
            category = int(split_line[0])
            minBilet = int(split_line[1])
            #Maksimum bilet sayısı M ile ifade edildiyse ilk dosyadan okunan maxBilet değerini alıyoruz
            if(split_line[2]=="M"):
               max_tickets=maxBilet
            else:
                max_tickets=int(split_line[2])
            indirim = int(split_line[3])
            indirimler.append((category, minBilet, max_tickets, indirim))
    # hata mesajı çıkarma
    if ticket_count > max_tickets:
        print('Maksimum bilet sayısı aşıldı!')
        exit()

    # toplam tutarı hesaplıyoruz
    total_price = ticket_count * fiyat[kategori - 1]

    # indirim uyguluyoruz
    indirimlifiyat = total_price
    for indirim in indirimler:
        if indirim[0] == kategori and indirim[1] <= ticket_count and ticket_count <= indirim[2]:
            indirimlifiyat = total_price - (total_price * indirim[3] / 100)
            toplamTutar[kategori-1]+=indirimlifiyat
            break


    if indirimlifiyat == total_price:
        toplamTutar[kategori - 1] += indirimlifiyat

    f = open('ciro.txt','w')
    for i in toplamTutar:
        f.writelines(str(i)+"\n")
    f.close()

    # toplam tutarı yazdırıyoruz
    print(f'Toplam tutar: {total_price} TL')
    print(f'Yapılan indirim: {total_price-indirimlifiyat} TL')
    print(f'Net tutar: {indirimlifiyat} TL')

def ToplamCiro():
    for i in range(len(toplamTutar)):
        print("Kategori "+str(i+1)+" Ciro:"+str(toplamTutar[i]))
    print("Toplam Ciro:",sum(toplamTutar))
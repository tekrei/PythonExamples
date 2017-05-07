from Ogrenci import *
#Bu metodun amaci parametre olarak adi verilen dosyayi acmak
#ve icerisindeki ogrenci bilgilerini bir dizi veri yapisina aktarmaktir
class OgrenciAraclar:
    def ogrencileriOku(self,dosyaAdi):
        #Dosyayi okumak icin aciyoruz
        f=open(dosyaAdi,'r')
        #Dosyadaki tum satirlari okuyoruz
        satirlar =f.readlines()
        #Ogrenci listesini yaratiyoruz
        ogrenciler = []
        #Dosyadan okudugumuz her satir icin
        for ogrenciBilgisi in satirlar:
            #Satirdaki ogrenci bilgisinden ogrenci nesnesini olusturup
            #listemize ekliyoruz
            ogrenciler.append(self.__ogrenciUret(ogrenciBilgisi))
        #ogrenci listemizi donduruyoruz
        return ogrenciler

    #Bu metodun amaci string olarak verilen ogrenci bilgisinden
    #Ogrenci sinifi ornegini olusturup dondurmektir
    def __ogrenciUret(self,ogrenciBilgisi):
        #String icerisindeki satir sonu karakterini yokediyoruz ve bosluklari kaldiriyoruz
        ogrenciBilgisi = ogrenciBilgisi.replace('\n',' ').strip()
        #Ogrenci bilgisi stringini saha parcalarina ayiriyoruz
        tokenler = ogrenciBilgisi.split('\t')
        #yeni ogrenci nesnesini tokenlerden olusturup donduruyoruz
        return Ogrenci(tokenler[0],tokenler[1],tokenler[2],tokenler[3])

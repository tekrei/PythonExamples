#OgrenciAraclar icerisindeki tum siniflari kullanacagiz
from OgrenciAraclar import *
#Yukaridaki metodu cagirip deniyoruz
ogrenciAraclar = OgrenciAraclar()
ogrenciler = ogrenciAraclar.ogrencileriOku('ogrenciler.txt');
#Okunan ogrenci bilgilerini ekrana yaziyoruz
for ogrenci in ogrenciler:
    print ogrenci.toString()

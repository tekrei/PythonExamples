#Ogrenci bilgilerini tuttugumuz sinif
class Ogrenci:
    #Yeni ogrenci yaratmak icin ilgili bilgilerini girmek gerekiyor
    #__init__ bu sinifin yapicisi oluyor
    def __init__(self, numara,isim,sinif,girisYili):
        #Basina __ ekleyince private degisken oluyor
        self.__isim = isim
        self.__numara = numara
        self.__sinif = sinif
        self.__girisYili = girisYili

    #Ogrenci bilgileri metin olarak donduren metod
    def toString(self):
        return self.__numara+' '+self.__isim+' '+self.__sinif+' '+self.__girisYili

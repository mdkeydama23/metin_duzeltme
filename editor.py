# Kullanıcının gireceği bir metin üzerinde, menü aracılığıyla
#
# -	Bul: kullanıcının gireceği bir metin parçasının bulunduğu yerlerin başlangıç konumlarını ekrana yazdırır
# -	Tümünü değiştir: kullanıcının gireceği bir metin parçasını, yine kullanıcının gireceği bir metin parçasıyla,
#   metin içerisinde bulunduğu her yerde değiştirir ve oluşan yeni metni ekrana yazdırır
# -	Tek tek değiştir: kullanıcının gireceği bir metin parçasını, yine kullanıcının gireceği bir metin parçasıyla,
#   metin içerisinde bulunduğu her yerde kullanıcı istiyorsa değiştirir ve oluşan yeni metni ekrana yazdırır
#
# işlemlerinin yapılabilmesini sağlayan bir program yazınız.

def menu_goruntule():
    print("1. Bul...")
    print("2. Tümünü değiştir...")
    print("3. Tek tek değiştir...")
    print("0. Çıkış...")
    print("Seçiminizi giriniz [0-3]:", end='')

def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input("hatalı veri girişi, lütfen tekrar giriniz:"))
    return sayi

def evet_hayir_al():
    cevap = input()
    while cevap not in "eEhH":
        cevap = input("hatalı veri girişi, lütfen tekrar giriniz:")
    return cevap

def bul(metin,aranan):
    bulunma_say=0
    aranan_uzunluk=len(aranan)
    print("No Konum")
    print("-- -----")
    bulunan_konum=metin.find(aranan)
    while bulunan_konum!=-1:
        bulunma_say+=1
        print(bulunma_say,"  ",bulunan_konum+1)
        bulunan_konum = metin.find(aranan,bulunan_konum+aranan_uzunluk)

def tumunu_degistir(metin,eski,yeni):
    return metin.replace(eski,yeni)

def tek_tek_degistir(metin,eski,yeni):
    aranan_uzunluk=len(eski)
    arama_baslangici=0
    yeni_metin=""
    bulunan_konum=metin.find(eski,arama_baslangici)
    while bulunan_konum!=-1:
        print(bulunan_konum+1,". konumdaki değiştirilsin mi(e/E/h/H)?:",sep="",end="")
        degisim=evet_hayir_al()
        yeni_metin = yeni_metin + metin[arama_baslangici:bulunan_konum]
        if degisim.upper()=="E":
            yeni_metin = yeni_metin+yeni
        else:
            yeni_metin = yeni_metin+eski
        arama_baslangici=bulunan_konum+aranan_uzunluk
        bulunan_konum = metin.find(eski,arama_baslangici)
    yeni_metin=yeni_metin+metin[arama_baslangici:]
    return yeni_metin

def main():
    metin=input("Metninizi giriniz:")
    cikis='H'
    while cikis.upper()=='H':
        menu_goruntule()
        menu_secim=sayi_al(0,3)
        if menu_secim==1:
            aranan=input("Aradığınız metin parçasını giriniz:")
            bul(metin,aranan)
        elif menu_secim==2:
            eski = input("Değiştirmek istediğiniz metin parçasını giriniz:")
            yeni = input("Yerine koymak istediğiniz metin parçasını giriniz:")
            metin=tumunu_degistir(metin,eski,yeni)
            print(metin)
        elif menu_secim==3:
            eski = input("Değiştirmek istediğiniz metin parçasını giriniz:")
            yeni = input("Yerine koymak istediğiniz metin parçasını giriniz:")
            metin=tek_tek_degistir(metin,eski,yeni)
            print(metin)
        else:
            print("Çıkmak istediğinizden emin misiniz(e/E/h/H)?:",end="")
            cikis=evet_hayir_al()

main()

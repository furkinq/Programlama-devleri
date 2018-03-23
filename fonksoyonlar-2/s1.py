def KDC(tsm,hm,bog,sg,sahg):
    global KDC
    KDC=tsm-(hm+bog+sg+sahg)
    if (KDC>=1000):
        print("İşletme Katma Değer Cirosu Yüksek")
    elif (500<KDC<999):
        print("İşletme Katma Değer Cirosu Normal")
    else:
        print("İşletme Katma Değer Cirosu Düşük")

tsm=int(input("Toplam Satış Miktarı:"))
hm=int(input("Hammadde Maliyeti:"))
bog=int(input("Bakım Onarım Giderleri:"))
sg=int(input("Sevkiyat Giderleri:"))
sahg=int(input("Satın Alınan Hizmet Giderleri:"))
sonuc=KDC(tsm,hm,bog,sg,sahg)
print(KDC)

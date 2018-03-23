satis_miktari=500
birim_satis_fiyati=20
ciro=5000
i=0
while (ciro<=500000):
    ciro=ciro+(satis_miktari*birim_satis_fiyati)
    satis_miktari=satis_miktari+200
    birim_satis_fiyati=birim_satis_fiyati+10
    i=i+1
print("Kârın 500.000 i geçmesi",i,"ay sürmüştür")






stock_miktari=10000
i=0
alinan_urun=100
satilan_urun=500
fark=alinan_urun-satilan_urun
while (stock_miktari>0):
    stock_miktari=stock_miktari+fark
    i=i+1
print(i)





#x=toplam
x=0
while True:
    print("Bir Sayı Giriniz(Çıkmak İçin '0' a Basınız):")
    girilen=int(input("Girilen Sayı:"))
    if(girilen!=0):
        y=girilen%3
        x=x+y
        print("Toplam=", x)
    else:
        print("Başarıyla Çıkış Yapıldı")
        break









gunluk_uretilen=200
gunluk_defolu_urun=0
toplam_defolu_urun=0
i=0
while (gunluk_defolu_urun<gunluk_uretilen*0.20):
    gunluk_defolu_urun=int(input("Günlük Defolu Ürün Miktarı:"))
    toplam_defolu_urun=toplam_defolu_urun+gunluk_defolu_urun
    i=i+1
    if(gunluk_defolu_urun>=gunluk_uretilen*0.20):
        print("Defolu Ürün Sayısı Limiti Aştı")
        break
print(i,"Günlük","Defolu Ürün Sayısı:",toplam_defolu_urun)









calisan=50
yevmiye=90
aylik_mesai=0
haftalik_maas=630
aylik_maas=0
while (aylik_mesai<=22):
    haftalik_mesai=int(input("Haftalık Mesai:"))
    aylik_mesai=haftalik_mesai*4
    haftalik_maas=haftalik_maas+(haftalik_mesai*yevmiye*0.10)
    aylik_maas=aylik_maas+haftalik_maas*4
    print("Aylık Maaş:",aylik_maas)
else:
    print("Aylık Mesai 22 Saatten Fazla Olamaz")














    

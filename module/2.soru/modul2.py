def aktif(kasa,alinanCek,bankaH,alacakSenetleri,ticariMal,binalar,tasitlar,demirbaslar):
    kasa=int(kasa)
    alinanCek=int(alinanCek)
    bankaH=int(bankaH)
    alacakSenetleri=int(alacakSenetleri)
    ticariMal=int(ticariMal)
    binalar=int(binalar)
    tasitlar=int(tasitlar)
    demirbaslar=int(demirbaslar)
    
    donenVarliklar=kasa+alinanCek+bankaH+alacakSenetleri+ticariMal
    print ("Dönen Varlıklar Toplamı:",donenVarliklar)
    
    duranVarliklar=binalar+tasitlar+demirbaslar
    print ("Duran Varlıklar Toplamı:",duranVarliklar)
    
    aktifToplami=donenVarliklar+duranVarliklar
    return aktifToplami



def pasif(bankaKredileri,saticilar,uzVadeliBankaKredileri,uzVadeliBorcSenedi,sermayeHesabi):
    bankaKredileri=int(bankaKredileri)
    saticilar=int(saticilar)
    uzVadeliBankaKredileri=int(uzVadeliBankaKredileri)
    uzVadeliBorcSenedi=int(uzVadeliBorcSenedi)
    sermayeHesabi=int(sermayeHesabi)

    
    kvyk=bankaKredileri+saticilar
    print("Kısa Vadeli Yabancı Kaynaklar Toplamı:",kvyk)
    
    uvyk=uzVadeliBankaKredileri+uzVadeliBorcSenedi
    print("Uzun Vadeli Yabancı Kaynaklar Toplamı:",uvyk)

    ozKaynaklar=sermayeHesabi
    print("Toplam Öz Kaynaklar:",ozKaynaklar)
    
    pasifToplami=kvyk+uvyk+ozKaynaklar
    return pasifToplami

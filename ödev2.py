def EEO():
    a=int(input("Planlanmış Üretim Süresi:"))
    b=int(input("plansız Duruş:"))
    c=int(input("Standart Çevrim Zamanı:"))
    d=int(input("Üretim Miktarı:"))
    e=int(input("Sağlam Ürün Miktarı:"))
    f=int(input("Toplam Ürün Miktarı:"))
    kullanılabilirlik=(a-b)/a
    performans=(c*d)/(a-b)
    kalite=e/f
    EEO=kullanılabilirlik*performans*kalite*100
    print("Ekipman Etkililik Oranı=" , EEO)

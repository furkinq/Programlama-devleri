from modul2 import*
aktifler=aktif(20000,10000,5000,28000,65000,150000,25000,8000)
pasifler=pasif(42000,60000,35000,115000,59000)
if aktifler==pasifler:
    print("bilanço doğru hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)
else:
    print("bilanço yanlış hesaplanmıştır.","aktif toplamı:",aktifler,"pasif toplami:",pasifler)

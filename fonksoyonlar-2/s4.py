#k=koltuk
#y=yatak
#d=dolap
def donemBasiStok(k1,y1,d1):
    global donemBasi
    donemBasi=k1+y1+d1
  
def donemSonuStok(k2,y2,d2):
    global donemSonu
    donemSonu=k2+y2+d2
  
def stokOrtalama(donemBasi,donemSonu):
    global ortalama
    ortalama=(donemBasi+donemSonu)/2

print("DÖNEM BAŞI STOK")
k1=int(input("Koltuk Adetini Giriniz:"))
y1=int(input("Yatak Adetini Giriniz:"))
d1=int(input("Dolap Adetini Giriniz:"))

print("DÖNEM SONU STOK")
k2=int(input("Koltuk Adetini Giriniz:"))
y2=int(input("Yatak Adetini Giriniz:"))
d2=int(input("Dolap Adetini Giriniz:"))

s1=donemBasiStok(k1,y1,d1)
s2=donemSonuStok(k2,y2,d2)
s3=stokOrtalama(donemBasi,donemSonu)
print("ORTALAMA STOK DEĞERİNİZ",ortalama)

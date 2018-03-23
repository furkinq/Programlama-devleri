#yg=yazılım geliri
#fg=finansal geliri
#usg=ürün satış geliri
#cm=çalışan maaşları
#kG=kira gideri
#dM=donanım maliyeti
#eTg=e ticaret geliri
#sg=sponsor geliri
def ilkAltiAyKar(yg1,fg1,usg1,cm1,kG1,dm1):
    global kar1
    kar1=(yg1+fg1+usg1)-(cm1+kG1+dM1)
    return kar1

def sonAltiAyKar(sg,eTg,yg2,fg2,usg2,cm2,kG2,dM2):
    global kar2
    kar2=(yg2+fg2+usg2+sg+eTg)-(cm2+kG2+dM2)
    return kar2

def karFark(kar1,kar2):
    fark=kar2-kar1
    if fark>5000:
        print(fark,"İŞLETME KARI ÇOKTUR")
    elif fark<1000:
        print(fark,"İŞLETME KARI DÜŞÜK")
    else:
        print(fark,"İŞLETME KARI NORMAL")
       
print("***İLK 6 AY*** ")
print("GELİRLER")
yg1=int(input("Yazılım gelirini giriniz="))
fg1=int(input("Finansman gelirini giriniz="))
usg1=int(input("Urun gelirini giriniz="))
print("GİDERLER")
cm1=int(input("Maaşlar giderini giriniz="))
kG1=int(input("Kira giderini giriniz="))
dM1=int(input("Donanım Giderini giriniz="))

print("***SON 6 AY***")
print("GELİRLER")
eTg=int(input("E-Ticaret geliri:"))
sg=int(input("Sponsor geliri:"))
yg2=int(input("Yazılım gelirini giriniz="))
fg2=int(input("Finansman gelirini giriniz="))
usg2=int(input("Urun gelirini giriniz="))
print("GİDERLER")
cm2=int(input("Maaşlar giderini giriniz="))
kG2=int(input("Kira giderini giriniz="))
dM2=int(input("Donanım Giderini giriniz="))

s1=ilkAltiAyKar(yg1,fg1,usg1,cm1,kG1,dM1)
s2=sonAltiAyKar(sg,eTg,yg2,fg2,usg2,cm2,kG2,dM2)
s3=karFark(kar1,kar2)


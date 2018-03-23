def mcs16(cs,tms):
    global tm
    tm=cs/tms

def mcs17(cs1,tms1):
    global tm1
    tm1=cs1/tms1

def fark(tm,tm1):
    global fark
    fark=tm-tm1
    

cs=int(input("2016 yılı için Çalışılan Süre:"))
tms=int(input("2016 yılı için Toplam Müşteri Sayisi:"))

print("**********************************")

cs1=int(input("2017 yılı için Çalışılan Süre:"))
tms1=int(input("2017 yılı için Toplam Müşteri Sayisi:"))

s1=mcs16(cs,tms)
s2=mcs17(cs1,tms1)
s3=fark(tm,tm1)
print("İki Yıl Arasındaki Fark:",fark)

def kar():
    a=int(input("Finansman Geliri:"))
    b=int(input("Pazar Geliri:"))
    c=int(input("Kira Geliri:"))
    d=int(input("Ücret:"))
    e=int(input("Finansman Gideri:"))
    f=int(input("Pazar Gideri:"))
    g=int(input("Kira Gideri:"))
    h=int(input("Muhasebe Gideri:"))
    ToplamGelir=a+b+c
    ToplamGider=d+e+f+g+h
    kar=ToplamGelir-ToplamGider
    if (0==kar):
        print("Denge Noktası")
    if (kar<=1000):
        print("Az Kârlı")
    elif(kar>1000):
        print("Kârlı" )
    else:
        print("Zararlı")
    return kar

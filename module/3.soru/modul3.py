class etkilesim:
    def __init__(self,begeniSayisi,yorumSayisi,paylasimSayisi,icerikSayisi,takipciSayisi):
        self.begeniSayisi=begeniSayisi
        self.yorumSayisi=yorumSayisi
        self.paylasimSayisi=paylasimSayisi
        self.icerikSayisi=icerikSayisi
        self.takipciSayisi=takipciSayisi
        etkilesimOrani=(((self.begeniSayisi + self.yorumSayisi + self.paylasimSayisi)/self.icerikSayisi)/self.takipciSayisi) * 100
        print("grup etkileşim oranı:",float(etkilesimOrani))
        if float(etkilesimOrani) >0.20:
            print("etkilesim oranı yüksek")
        else:
            print("etkilesim oranı düşük")

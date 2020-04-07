class NaZakupy():
    def __init__ (self,nazwa,ilosc,cena,miara):
        self.nazwa="mleko"
        self.ilosc=ilosc
        self.miara="litry"
        self.cena= cena 

    def wyswietl_produkt(self):
            nazwa= self.nazwa
            cena=self.cena
            return nazwa,cena
    def ile_produktu(self):
        print(self.ilosc)
        print(self.miara)
    def ile_kosztuje(self,cena,ilosc):
        return self.cena*self.ilosc

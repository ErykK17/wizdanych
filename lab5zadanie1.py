class material:
    def __init__ (self,rodzaj, dlugosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        return self.rodzaj
class ubrania(material):
    def __init__ (self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        return self.rozmiar,self.kolor,self.dla_kogo
class swetry(ubrania):
    def __init__ (self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        return self.rodzaj_swetra


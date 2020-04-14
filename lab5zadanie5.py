class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

iojozek=isinstance(jozek,Osoba)
ioadrian=isinstance(adrian,Osoba)
ipjozek=isinstance(jozek,Pracownik)
ipadrian=isinstance(adrian,Pracownik)
imjozek=isinstance(jozek,Menadzer)
imadrian=isinstance(adrian,Menadzer)

prac=issubclass(Pracownik,Osoba)
men=issubclass(Menadzer,Osoba)

if iojozek:
    print("jest instancja klasy osoba")
else:
    print ("nie jest instancja klasy osoba")

if ioadrian:
    print("jest instancja klasy osoba")
else:
    print ("nie jest instancja klasy osoba")

if ipjozek:
    print("jest instancja klasy pracownik")
else:
    print ("nie jest instancja klasy pracownik")

if ipadrian:
    print("jest instancja klasy pracownik")
else:
    print ("nie jest instancja klasy pracownik")

if imjozek:
    print("jest instancja klasy menadzer")
else:
    print ("nie jest instancja klasy menadzer")

if ipadrian:
    print("jest instancja klasy menadzer")
else:
    print ("nie jest instancja klasy menadzer")


if prac:
    print ("jest subklasa")
else:
    print("niejest subklasa")

if men:
    print ("jest subklasa")
else:
    print("niejest subklasa")
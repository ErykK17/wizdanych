class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __add__(self,kwadrat):
        return Kwadrat(self.x + kwadrat.x)
    def __ge__ (self,kwadrat):
        if self.x >= kwadrat.x:
            return Kwadrat(self.x)
    def __gt__ (self,kwadrat):
        if self.x > kwadrat.x:
            return Kwadrat(self.x)
    def __le__ (self,kwadrat):
        if self.x <= kwadrat.x:
            return Kwadrat(self.x)
    def __lt__ (self,kwadrat):
        if self.x < kwadrat.x:
            return Kwadrat(self.x)
    def __str__(self):
        return f'Kwadrat ({self.x})'    

k1=Kwadrat(3)
k2=Kwadrat (5)

if k1>=k2:
    print(k1)
else:
    print(k2)

if k1>k2:
    print(k1)
else:
    print(k2)

if k1<=k2:
    print(k1)
else:
    print(k2)

if k1<k2:
    print(k1)
else:
    print(k2)


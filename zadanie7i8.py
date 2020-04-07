class robaczek:
  def __init__ (self,x,y,krok):
    self.x=x
    self.y=y
    self.krok=krok
  def __del__(self):
    print("obiekt usuniety")  
  def gora(self):
    self.y+=self.krok
  def dol (self):
    self.y-=self.krok
  def lewo (self):
    self.x-=self.krok
  def prawo (self):
    self.x+=self.krok
  def gdziejestem(self):
    print (self.x,self.y)

r=robaczek(1,5,2)
r.gora()
r.gora()
r.gora()
r.lewo()
r.lewo()
r.lewo()
r.prawo()
r.prawo()
r.prawo()
r.prawo()
r.gdziejestem()
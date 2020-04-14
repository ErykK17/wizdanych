class samogloski:
    def __init__(self, dane):
        self.dane=dane
        self.index= -1  
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==len(self.dane):
            raise StopIteration
        self.index= self.index +1
        samogloski=("a","e","i","o","u","A","E","I","O","U")
        if self.dane[self.index] in samogloski:
            return self.dane[self.index]


asd=("Piesek")
it = samogloski(asd)
print (it)
print (next(it))
print (next(it))
print (next(it))
print (next(it))
print (next(it))


x=isinstance(asd,str)
if x :
    print ("string")
else:
     print ("nie string")
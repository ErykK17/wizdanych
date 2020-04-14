class parzyste:
    def __init__(self, dane):
        self.dane=dane
        self.index= 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==len(self.dane):
            raise StopIteration
        self.index= self.index +1
        if (self.index % 2==0):
            return self.dane[self.index]

asd=[1,2,3,4,5]
it = parzyste(asd)
print (it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
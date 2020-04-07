plik=open("plik.txt","w+")
numery=[]
for n in range (0,200):
    if n%4==0:
        numery+= [n]
plik.write(str(numery))
plik.close()

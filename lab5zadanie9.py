def parzyste(lista):
    for i in lista:
        i=i-1
        if i%2==0:
            yield lista[i]

asd=[1,2,3,4,5,6,7,8,9]
for liczba in parzyste(asd):
    print (liczba)
with open("tekst.txt","r+")as plik:
    plik.write(str("asdf"))
    lista=plik.readlines()
print (lista)
    
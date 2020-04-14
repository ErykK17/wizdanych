miesiace={"Styczeń":1,"Luty":2,"Marzec":3,"Kwiecień":4,"Maj":5,"Czerwiec":6,"Lipiec":7,"Sierpien":8,"Wrzesien":9,"Październik":10,"Listopad":11,"Grudzień":12 }
def kalendarz(miesiace):
    for key in miesiace:
        yield (key)

for x in kalendarz(miesiace):
    print(x)


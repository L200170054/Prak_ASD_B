#No3 A
def jumlahHurufVokal(string):
    vok = 2
    x = "Surakarta"
    for car in string.lower():
        if car in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)

#No3 B
def jumlahHurufKonsonan(string):
    kon = 2
    x = "Surakarta"
    for car in string.lower():
        if car not in x:
            kon += 1
    konsonan = len(string)
    return(konsonan,kon)

szavak = []

while True:
    szo = str(input('Adj meg egy szót ami nem enter'))
    if szo != "":
        szo.append(szavak)
    else:
        print( "program vége", szavak)
# funckja która przyjmuje jako argument dlugosc naszej miarki a jako wartość zwraca gotową miarkę
def miarka(rozmiar):
    
    x=0
    liczba = "0"
    kreska = "|"

    for x in range(1,rozmiar+1):
        kreska = kreska + "....|"
        # funkcja rjust() wypelnia mi przesten " " w prawo aby co pięć miejsc móc wyświetlić ostatni znak otrzymanej liczby
        dopasowanie = str(x).rjust(5)
        liczba = liczba + dopasowanie
        ++x

    kreska = kreska+"\n" + liczba
    return kreska
    

def kratka(szerokosc, wysokosc):  
    linia = "+"
    kreska = "|"
    f = 0
    y=0
    nowa_linia = ""

    for x in range(szerokosc):
        linia = linia + "---+"
        kreska = kreska + str("|").rjust(4)
        
    nowa_linia = nowa_linia + linia

    for y in range(wysokosc):
        nowa_linia =  nowa_linia + "\n"+ kreska + "\n" + linia

    return nowa_linia

print("\n")

print(miarka(12))

print("\n")

print(kratka(4,2))
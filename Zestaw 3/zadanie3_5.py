print("\nProgram rysujacy miarke o zadanej dlugosci")
rozmiar =int(input("\nWprowadz dlugosc miarki: "))
print("\n")

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
    
    
print(miarka(rozmiar))




print("\n\nProgram który dopełnia liczby zerami, aby wszystkie miały długość trzy \n")

lista = []

# jako iż chcemy zmienną jako pewna liczba to musimy zadeklarować ze ta zmienna ma mieć postać int
ilosc_liczb = int(input("Podaj jaką ilość liczb całkowitych dodatnich chcesz wprowadzić do listy: "))
print("\n")


x = 0

# tutaj x jest naszym iteratorem który jeździ po funkcji range od zera do dowolnie dużej wprowadzonej przez użytkownika liczby, kieddy x będzie równe najwiekszej liczbe z range to pętla się zatrzymuje
for x in range(0, ilosc_liczb) :
    liczba = input("Wprowadz maksymalnie 3-cyfrową liczbę do listy: ")
    print("\n")

    # funkcja append dołącza nam kolejne cyfry na koniec listy
    lista.append(liczba)
    ++x


m = 0

for m in range(len(lista)) :
    # lista[m] gdzie m to iterator który będzie nam jeździł od pierwszej liczby do ostatniej i funkcja zfill() wypełni zerami z przodu daną liczbę, tak aby jej długość wyniosła 3
    print(lista[m].zfill(3))
    ++m


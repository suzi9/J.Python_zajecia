print("\n\nProgram tworzy napis będący ciągiem cyfr kolejnych liczb z listy\n")

lista = []

# jako iż chcemy zmienną jako pewna liczba to musimy zadeklarować ze ta zmienna ma mieć postać int
ilosc_liczb = int(input("Podaj jaką ilość liczb całkowitych dodatnich chcesz wprowadzić do listy: "))
print("\n")


x = 0

# tutaj x jest naszym iteratorem który jeździ po funkcji range od zera do dowolnie dużej wprowadzonej przez użytkownika liczby, kieddy x będzie równe najwiekszej liczbe z range to pętla się zatrzymuje
for x in range(0, ilosc_liczb) :
    liczba = input("Wprowadz liczbę do listy: ")
    print("\n")

    # funkcja append dołącza nam kolejne cyfry na koniec listy
    lista.append(liczba)
    ++x
    

# za pomocą "".join(lista), łączymy wszytskie cyfry listy w jeden napis
napis = "".join(lista)

print("Stworzony napis to: ", napis)
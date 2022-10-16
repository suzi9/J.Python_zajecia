print("\n\nProgram znajduję najdłuższy wyraz w zdaniu i oblicza jego długość\n")

zdanie = input("Wpisz dowolne zdanie: ")

lista = zdanie.split()

najdluzszy_wyraz = max(lista, key = len)

print("\nNajdluzszy wyraz w zdaniu to: ",najdluzszy_wyraz)

dlugosc_najdluzszego_wyrazu = len(najdluzszy_wyraz)

print("\nDlugosc najdluzszego wyrazu wynosi: ",dlugosc_najdluzszego_wyrazu )

print("\n\nProgram oblicza liczbę wyrazów w napisie\n")

zdanie = input("Wpisz dowolne zdanie: ")

zdanie_bez_znakow_bialych = zdanie.split()

print("Liczba wyrazów w napisie wynosi: ", len(zdanie_bez_znakow_bialych))


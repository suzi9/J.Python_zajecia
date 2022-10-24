sekwencja1 = input("\nWprowadz pierwsza sekwencje zlozona z liczb i znakow: ")
sekwencja2 = input("\nWprowadz druga sekwencje zlozona z liczb i znakow: ")
print("\n")
wynik = set(sekwencja1).intersection(sekwencja2)
print("-------------------------------------------------------------------------------------")
print("Elementy wystepujace jednoczesnie w obu sekwencjach: ",wynik)
print("-------------------------------------------------------------------------------------\n")

# za pomocą funkcji set wypisujemy wszystkie elementy danej sekwencji bez powtorzen
wynik_2 = set(sekwencja1)
wynik_3 = set(sekwencja2)
print("-------------------------------------------------------------------------------------")
print("Wszystkie elementy wystepujace w sekwencji pierwszej: ", wynik_2)
print("-------------------------------------------------------------------------------------\n")

print("-------------------------------------------------------------------------------------")
print("Wszystkie elementy wystepujace w sekwencji drugiej: ", wynik_3)
print("-------------------------------------------------------------------------------------\n")

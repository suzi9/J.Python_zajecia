
print("\n\nProgram znajduję łączną długość wyrazów w zdaniu\n")

wprowadzone_zdanie = input("Wpisz dowolne zdanie: ")
lista = wprowadzone_zdanie.split()

wyraz=0
laczna_dlugosc_wyrazow=0

for wyraz in range(len(lista)):
    laczna_dlugosc_wyrazow = laczna_dlugosc_wyrazow + len(lista[wyraz]) 
    ++wyraz

print("Łączna długość wyrazów wynosi: ", laczna_dlugosc_wyrazow)
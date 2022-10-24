
print("\n\nProgram wyświetla napis stworzony z pierwszych i ostanich znków wyrazów z wprowadzonego zdania\n")
 
zdanie = input("Wpisz dowolne zdanie: ")

zdanie_bez_znakow_bialych = zdanie.split()

zdanie_bez_znakow_bialych_2 = zdanie_bez_znakow_bialych

x =0

i = 0
napis_ze_znakow_pierwszych = ""


for x in range(len(zdanie_bez_znakow_bialych)) :
    napis = zdanie_bez_znakow_bialych[x][i]
    napis_ze_znakow_pierwszych = napis_ze_znakow_pierwszych + napis
    ++x


print("\nNapis z pierwszych znaków każdego słowa to :", napis_ze_znakow_pierwszych)


m = 0
napis_ze_znakow_ostatnich = ""

for m in range(len(zdanie_bez_znakow_bialych_2)):      
    napis = zdanie_bez_znakow_bialych_2[m][-1]
    napis_ze_znakow_ostatnich = napis_ze_znakow_ostatnich + napis
    ++m

print("\nNapis z ostatnich znaków każdego słowa to :", napis_ze_znakow_ostatnich)
x = 0

print("\nProgram wypisuje liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3\n")

for x in range(30):
    # robie x modulo 3, ponieważ jeśli dostaniemy resztę to znaczy że liczba nie jest podzielna przez 3
    if x % 3 != 0:
        print(x)
  



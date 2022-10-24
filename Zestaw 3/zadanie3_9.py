sekwencja = [[], [4], (1,2), [3,4], (5,6,7)]
lista = []

for x in sekwencja:
    # funkcja .append() dodaje nam kolejne sumy elemntow na koniec listy
    # sum() zlicza nam wspolna sume danych elementow czy to w liscie czy w krotce
    lista.append(sum(x))

print(lista)

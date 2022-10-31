def sum_seq(sekwencja):
    lista = []
    for x in sekwencja:
        lista.append(sum(x))
    
    wynik = 0
    for i in range(len(lista)):
        wynik = wynik + lista[i]

    return wynik

sekwencja = [[], [4], (1,2), [3,4], (5,6,7)]
print(sum_seq(sekwencja))
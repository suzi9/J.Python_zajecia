def sum_seq(sekwencja):
    lista = []
    for x in sekwencja:
        if isinstance(x, (list, tuple)):
            lista = lista + sum_seq(x)
        else:
            lista.append(x)
    
    return lista
    

sekwencja = [1,(2,3),[],[4,(5,6,7)],8,[9]]

lista_wynik = sum_seq(sekwencja)

print(sum(lista_wynik))
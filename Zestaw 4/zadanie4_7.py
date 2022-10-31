
def flatten(sekwencja):
    lista = []
    for x in sekwencja:
        if isinstance(x, (list, tuple)):
            lista = lista + flatten(x)
        else:
            lista.append(x)

    return lista
    

sekwencja = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(flatten(sekwencja))
import math

def odwracanie_iteracyjnie(L, left, right):
    liczba_elementow = right-left # odejmujemy ostani indeks od pierwszego
    liczba_zamiany = math.ceil(liczba_elementow / 2) # obliczamy liczbę zamian która będzie potrzebna do ułożenia listy

    for i in range(liczba_zamiany): 
        L[left], L[right] = L[right], L[left] # wykonujemy zamiane dla elementów
        left = left + 1
        right = right - 1
        
    return L
      

def odwracanie_rekurencyjne(L, left, right):
    if right > left:
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1
        odwracanie_rekurencyjne(L,left, right)
    return L


L = [1,2,3,4,5,6,7,8,9,10,11]

kopia_listy = L.copy()

print("Lista odwrocona iteracyjnie: ",odwracanie_iteracyjnie(L, 0, 6)) # jako argumenty podajemy indeksy

print("Lista odwrocona rekurencyjnie",odwracanie_rekurencyjne(kopia_listy, 0, 6)) 

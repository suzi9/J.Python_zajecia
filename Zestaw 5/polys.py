
def add_poly(poly1, poly2):        # poly1(x) + poly2(x)
    # liczba - odowiada za długość listy  -> to to jak długa będzie lista wynikowa 
    liczba = 0
    # jeżeli lista poly1 jest większa od poly 2 
    if len(poly1) > len(poly2):
        # to lista wynikowa ma długość poly1
        liczba = len(poly1)
        # a do poly2 od ostatniego indeksu
        # dodajemy 0 do poly2 aby ją rozszerzyć by móc wykonywać dodawanie, rozszerzamy ją zerami aż do indeksu liczba-1, -1 bo zaczynamy od zera
        for i in range(liczba-1):
            poly2.append(0)
    # w przeciwnym wypadku kieddy poly2 jest większa od poly1, wykonujemy analogiczne kroki, tylko że na odwrót z wartościami
    else:
        liczba = len(poly2)
        for i in range(liczba-1):
            poly1.append(0)
    
    poly3 = []
    a = 0
    dany_wynik = 0

    for a in range(liczba):
        dany_wynik = poly1[a] + poly2[a]
        poly3.append(dany_wynik)

    return poly3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    # liczba - odowiada za długość listy  -> to to jak długa będzie lista wynikowa 
    liczba = 0
    # jeżeli lista poly1 jest większa od poly 2 
    if len(poly1) > len(poly2):
        # to lista wynikowa ma długość poly1
        liczba = len(poly1)
        # a do poly2 od ostatniego indeksu
        # dodajemy 0 do poly2 aby ją rozszerzyć by móc wykonywać dodawanie, rozszerzamy ją zerami aż do indeksu liczba-1, -1 bo zaczynamy od zera
        for i in range(liczba-1):
            poly2.append(0)
    # w przeciwnym wypadku kieddy poly2 jest większa od poly1, wykonujemy analogiczne kroki, tylko że na odwrót z wartościami
    else:
        liczba = len(poly2)
        for i in range(liczba-1):
            poly1.append(0)
    
    poly3 = []
    a = 0
    dany_wynik = 0

    for a in range(liczba):
        dany_wynik = poly1[a] - poly2[a]
        poly3.append(dany_wynik)

    return poly3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    poly3 = []
    # obliczamy łączną długość obu list razem, i od zera do tej łącznej długości wypełniamy listę poly3 zerami aby następnie móc na niej wykonywać operację
    for i in range(0, len(poly1) + len(poly2)-1):
        poly3.append(0)

    for a in range(len(poly1)):
        for j in range(0,len(poly2)):
            poly3[a + j] = poly3[a+j] + poly1[a] * poly2[j]

    return poly3
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_zero(poly):                # bool, [0], [0,0], itp.
    # funkcja all zwraca wartość true jeżeli wszystkie wartości listy wynoszą zero
    if all([i == 0  for i in poly]):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def eq_poly(poly1, poly2):       # bool, porównywanie poly1(x) == poly2(x)
    if set(poly1) == set(poly2):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def eval_poly(poly, x0):         # poly(x0), algorytm Hornera
    wynik = poly[0]
    
    # algorytm Hornera
    for j in range(1, len(poly)):
        wynik = wynik * x0 + poly[j]

    return wynik


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def pow_poly(poly, n):    # poly(x) ** n
    
    wynik = [1]
    
    for j in range(n):
        wynik = mul_poly(wynik, poly)

    return wynik

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def diff_poly(poly):      # pochodna wielomianu
    wynik = []
    i = 0
    for i in range(len(poly)):
        dana_wartosc = poly[i] * i
        wynik.append(dana_wartosc)

    return wynik

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def combine_poly(poly1, poly2):  # poly1(poly2(x)), trudne!
    wynik = [0, 0]

    for i, pozycja in enumerate(poly1):
        wynik = add_poly(wynik, [pozycja * j for j in pow_poly(poly2, i)])
        
    return wynik

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

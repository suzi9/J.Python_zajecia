# Poniższy kod jest napisany poprawnie składniowo
# Jedyne co to można napisać te dwie instrukcję w osobnych liniach
# Bo ten średnik wydaje się zbędny
# L = [3, 5, 4]
# L = L.sort()

L = [3, 5, 4] ; L = L.sort()

#-----------------------------------------------------------------------------

# W poniższym kodzie dostaniemy błąd ponieważ próbujemy przypisać 
# 3 wartości tylko dwóm zmiennych, poniższy problem można rozwiązać w ten sposób:
# kod ten możemy zapisać x,y = 1,2  albo x,y,z = 1, 2, 3 , wtedy rozwiążemy ten błąd
x, y = 1, 2, 3

#-----------------------------------------------------------------------------

# Natomiast w tym poniższym kodzie to jak wartości są przypisane do zmiennej X,
# powoduje że to tworzy krotke
# A przy kolejnej operacji: X[1] = 4 jest próba zmienienia tej wartości w środku krotki
# i przez to dostajemy błąd ponieważ jest to operacja zabroniona
X = 1, 2, 3 ; X[1] = 4

#-----------------------------------------------------------------------------

# W poniższym kodzie mamy próbę przypisania do indeksu 3 w liście pewnej wartości
# Ale jako iż ten indeks nie istnieje to dostajemy błąd
# Ponieważ w liście X = [1, 2, 3], mamy indeksy 0, 1 i 2
X = [1, 2, 3] ; X[3] = 4

#-----------------------------------------------------------------------------

# Metody .append() nie możemy używać do zmiennych typu string, daltego dostaniemy błąd
# Tylko w przypadku jeśli X byłaby listą to metoda mogła by zostać użyta
# Za to uważam iż aby dodać do stringa kolejnego stringa to można użyć konkatenaji
X = "abc" ; X.append("d")

#-----------------------------------------------------------------------------

# Jako iż funkcja pow() nie dostaje na wejściu argumentów to dostajemy błąd
L = list(map(pow, range(8)))

#-----------------------------------------------------------------------------
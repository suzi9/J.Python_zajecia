import itertools as it
import random as rd

print("\na) iterator zwracający 0, 1, 0, 1,...\n")
print("b) iterator zwracający przypadkowo jedną wartość\n")
print("c) iterator zwracający numery dni tygodnia\n")


a = input("\nWybierz ktory podpunkt zadania chcesz wykonac: ")
f = 0
match a:
    case 'a':
        dwie_liczby = it.cycle([0, 1])
        for i in range(30):
            print(next(dwie_liczby))

    case 'b':
        bladzenie_przypadkowe = iter((lambda: rd.choice(("N", "E", "S", "W"))), 1)
        for i in range(30):
            print(next(bladzenie_przypadkowe))

    case 'c':
        liczba_dni_tygodnia = it.cycle(i for i in range(7))
        for i in range(30):
            print(next(liczba_dni_tygodnia))

# funkcja obliczająca siline iteracyjnie
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        i=1
        wynik = 1
        for i in range(n):
            wynik = wynik * (i+1)
        return wynik


print("\nSilnia wynosi: ",factorial(8), "\n")
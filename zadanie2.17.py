print("\n\nProgram sortuje wyrazy zdania alfabetycznie a potem pod względem długości wyrazów\n")

zdanie = input("Wpisz dowolne zdanie: ")

lista_wyrazow = zdanie.split()

# robie sobie kopie oryginalnej listy 
kopia_listy_wyrazow = lista_wyrazow

# za pomocą funkcji sorted(), wyrazy sortują sie alfabetycznie
sortowanie_alfabetyczne = sorted(lista_wyrazow)

# za pomocą funkcji join, wyświetlam posortowane alfabetycznie wyrazy w postaci string
print("\nWyrazy posortowane alfabetycznie: "," ".join(sortowanie_alfabetyczne))

# za pomocą funkcji sorted() i argumentu key = len, wyrazy sortują się pod względem długości
sortowanie_pod_wzgledem_dlugosci = sorted(kopia_listy_wyrazow, key = len)

# za pomocą funkcji join, wyświetlam posortowane według długości wyrazy w postaci string
print("\nWyrazy posortowane pod względem długości: "," ".join(sortowanie_pod_wzgledem_dlugosci))
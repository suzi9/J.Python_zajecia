print("\n\nProgram znajduję liczbę cyfr 0, które występują w liczbie całkowitej\n")

# używam int() aby dać znać że to co wczytujmey to liczba całkowita
liczba = int(input())

# za pomocą funkcji count() liczymy ile jest zer w liczbie, gdzie str(liczba), zamienia nam liczbę na napis
illosc_zer = str(liczba).count('0')

print("\nIlość zer w wprodzonej liczbie wynosi: ",illosc_zer)
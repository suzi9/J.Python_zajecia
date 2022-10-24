print("\nProgram który konwertuje podaną liczbę rzymską na arabską\n")
# tutaj naszymi kluczami są cyfry rzymskie a wartościami cyfry arabskie
slownik = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,"D": 500,"M": 1000}

liczba_rzymska = input("Wprowadz liczbe rzymską: ")

liczba_arabska = slownik[liczba_rzymska]

print("Odpowiednik w liczbach arabskich to: ",liczba_arabska)
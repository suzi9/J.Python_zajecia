def fibonacci(n):
    if n == 0 or n == 1 or n== 2 :
        return 1
    
    else:
        wynik = 0
        przed_w = 1

        for i in range(0, n):
            wynik, przed_w = przed_w, wynik + przed_w
        return wynik

print(fibonacci(8))

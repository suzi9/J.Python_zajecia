print("\nProgram pobiera liczbe i potem ją wyswietla oraz jej trzecia potege")

x = ""

# ustawiam pętle while na True przez to będzie wykonywać się w nieskończoność lub dopóki jej nie przerwiemy
while True :
    print("\n-----------------------------------------------")
    x = input("Wprowadz dowolna liczbe lub wpisz 'stop' jesli chcesz zakonczyc program: ")

    if x != "stop":
        # jeśli x będzie literą to wtedy to będzie Prawda, więc pętla nam się będzie wykonywać dopóki x nie będzie literą
        while x.isalpha() == True: 
            print("\nBlad, podales napis zamiast liczby")
            x = input("Wprowadz liczbe aby kontynuowac: ")
            if x == "stop":
                # ten break wychodzi nam z aktualnej pętli i przechodzi do drugiej pętli
                break
            
        # a ten break wychodzi nam już całkowicie pętle i zakańcza program
        if x=="stop": break
        # kiedy już mamy pewność że x to liczba to konwertujemy ją na typ float   
        f = float(x)
        print("\nPodana liczba to: ",f," jej trzecia potega to: ", f**3)

    # kiedy wpiszemy słowo "stop" to break nam przerwie wykonanie się pętli
    else:
        break

   




import tkinter as tk
from tkinter import ttk
import pandas
from tkinter import scrolledtext
from tkinter import messagebox
import csv

class Aplikacja(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #Jeżeli nie dostarczymy prametru to przyjmiemy wartość None
        self.okno = None
        self.zmiana_okna(Menu)
        # nazwa okienka
        self.title("Baza danych książek")
        # funkcja geometry() służy do ustawiania wymiarów okna Tkintera 
        self.geometry("750x600")

    def zmiana_okna(self, klasa_okna):
        # Niszczy bieżący Frame i zastępuje go nowym Frame
        nowe_okno = klasa_okna(self)

        if self.okno is not None:
            self.okno.destroy()

        self.okno = nowe_okno
        self.okno.pack()

class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="BAZA DANYCH KSIĄŻEK", font="Times 35 bold", 
              width= 50, height= 0).pack()
        tk.Label(self, text="Wybierz jaką akcje chcesz wykonać:", 
              font="Times 20", width= 50, height= 2).pack()

        #Przyciski
        tk.Button(self,bg="#D3D3D3", text = "Wyświetl bazę książek", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Wyswietlanie)).pack()

        tk.Button(self,bg="#D3D3D3", text = "Dodaj nową książke", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Dodawanie)).pack()

        tk.Button(self,bg="#D3D3D3", text = "Usuń książke", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2",
                command= lambda: master.zmiana_okna(Usuwanie)).pack()
        
        tk.Button(self,bg="#D3D3D3", text = "Znajdź książkę", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2",
                command= lambda: master.zmiana_okna(Wyszukiwanie)).pack()

        # Prycisk który zakańcza pracę programu
        tk.Button(self,bg="#D3D3D3",text = "Zamknij", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.destroy()).pack()

class Wyswietlanie(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="LISTA WSZYSTKICH KSIĄŻEK W BAZIE", 
              font="Times 20 bold", width= 50, height= 0).pack()

        #Wyświetlanie bazy w okienku którym jest możliwość scrollowania
        # read_csv() pochodzi z modułu pandas
        otwarcie_bazy= pandas.read_csv('baza.csv')
        wyswietlanie_w_okienku = scrolledtext.ScrolledText(self,  width=80, 
                                                            height=29)
        wyswietlanie_w_okienku.pack()
        wyswietlanie_w_okienku.insert(tk.INSERT, otwarcie_bazy)

        # Konfiguruje wyświetlanie w okienku tylko do odczytu (read-only)
        wyswietlanie_w_okienku.configure(state='disabled')

        #Przyciski
        tk.Button(self, bg="#D3D3D3",text = "Powrót do strony głównej", 
           height=3,width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Menu)).pack()

class Dodawanie(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="DODAJ NOWĄ KSIĄŻKĘ", font="Times 35 bold", 
               width= 50, height= 0).pack()

        #Wpowadzanie identyfikatora
        tk.Label(self, text="Podaj identyfikator książki",
                font="Times 13").pack()
        wprowadz_id = tk.Entry(self, width=60)
        # ipady używam do ustawienia wyskości pola o wpisywania czyli entry
        wprowadz_id.pack(ipady=15)

        #Wprowadzanie tytułu
        tk.Label(self, text="Podaj tytuł książki",font="Times 13").pack()
        wprowadz_tytul = tk.Entry(self, width=60)
        wprowadz_tytul.pack(ipady=15)

        #Wprowadzanie autora
        tk.Label(self, text="Podaj autora książki",font="Times 13").pack()
        wprowadz_autora = tk.Entry(self, width=60)
        wprowadz_autora.pack(ipady=15)

        #Wprowadzanie roku
        tk.Label(self, text="Podaj rok wydania książki",font="Times 13").pack()
        wprowadz_rok = tk.Entry(self, width=60)
        wprowadz_rok.pack(ipady=15)

        def dodaj_ksiazke(wprowadz_id, wprowadz_tytul, wprowadz_autora, 
                         wprowadz_rok):
            
            otwarcie_bazy= pandas.read_csv('baza.csv')

            #Pobranie identyfikaora ksiazki
            identyfikator = int(wprowadz_id.get())

            # Jeżeli podany identyfikator książki nie istnieje to dodamy 
            # książke do bazy
            if identyfikator not in otwarcie_bazy['ID'].values:
                id_ksiazki = str(identyfikator)

                #Pobranie tytulu ksiazki
                tytul = wprowadz_tytul.get()

                #Pobranie autora ksiazki
                autor = wprowadz_autora.get()

                #Pobranie roku wydania ksiazki
                rok = wprowadz_rok.get()
                if rok.isnumeric():
                   rok_ksiazki = str(rok)

                zlaczone_dane = id_ksiazki+','+ tytul+','+ autor + ','+ rok_ksiazki
                wszystkie_dane=[zlaczone_dane]
                zapisac_dane = pandas.DataFrame(wszystkie_dane)

                # używam escapechar i quoting aby do pliku .csv zapisywac 
                # dane bez cudzysłowów, żeby mi się poprawnie baza wyświetlała
                zapisac_dane.to_csv('baza.csv', index=False, mode='a', 
                  header=False, escapechar=' ' , quoting=csv.QUOTE_NONE)

            # w przeciwnym wypadku dajemy komunikat użytkownikowi że książka 
            # o takim ID już istnieje 
            else:
                messagebox.showwarning("Uwaga!",
                "Podany identyfikator już istnieje w bazie danych książek."
                "\nProsimy o podanie innego ID!")

        
        # Funkcja do czysczenia pól entry -> tam gdzie się wrowadza dane
        def wyczysc_dane(wprowadz_id, wprowadz_tytul, wprowadz_autora, 
                        wprowadz_rok):
            wprowadz_id.delete(0, tk.END)
            wprowadz_tytul.delete(0, tk.END)
            wprowadz_autora.delete(0, tk.END)
            wprowadz_rok.delete(0, tk.END)


        # Aby móc dodać dwa przyciski obok siebie tworzę nowy Frame w tym 
        # samym okienku i  w tym Frame je tam umieszcze   
        top = tk.Frame(self)
        # i wyświetlam go z pozycją u góry
        top.pack(side=tk.TOP)

        #Przyciski
        # Parametr in_= pozwala umieścić widżet w innym kontenerze, o ile 
        # argument „in_” jest potomkiem rodzica
        tk.Button(self,bg="#D3D3D3", text="Zapisz", fg="#3da063",cursor="hand2"
                , width=20, height=3 ,font= "Times 10 bold" , 
                command=lambda:dodaj_ksiazke(wprowadz_id, wprowadz_tytul,
                 wprowadz_autora, wprowadz_rok)).pack(side=tk.LEFT, in_=top)

        tk.Button(self,bg="#D3D3D3", text="Wyczyść",fg="#4700ff",
                cursor="hand2", width=20, height=3 ,font= "Times 10 bold" , 
                command=lambda:wyczysc_dane(wprowadz_id, wprowadz_tytul,
                wprowadz_autora, wprowadz_rok)).pack(side=tk.RIGHT, in_=top)

        tk.Button(self,bg="#D3D3D3", text = "Powrót do strony głównej", 
                height=4, width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Menu)).pack()

class Usuwanie(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="USUŃ KSIĄŻKĘ", font="Times 35 bold",
               width= 50, height= 0).pack()

        tk.Label(self, text="Wprowadz ID książki którą chcesz usunąć",
               font="Times 13").pack()

        wprowadz_id_ksiazki = tk.Entry(self, width=60)
        # ipady używam do ustawienia wyskości pola o wpisywania czyli entry
        wprowadz_id_ksiazki.pack(ipady=15)

        def usuwanie_ksiazki(wprowadz_id_ksiazki):
            #Pobranie identyfikaora ksiazki
            identyfikator = wprowadz_id_ksiazki.get()
            if identyfikator.isnumeric():
                id_ksiazki = int(identyfikator)

            otwarcie_bazy= pandas.read_csv('baza.csv')
            
            # Zmienna która przechowuje całą kolumnę ID
            identyfikator = otwarcie_bazy['ID']

            # Jeżeli podany przez użytkownika identyfikator książki istnieje 
            # w wartościach kolumny ID to wykonają się instrukcje dla if
            if id_ksiazki in identyfikator.values:
                # Wiadomość będzie nam zwracać wartość True jeśli użytkownik 
                # kliknie "Tak" i wartość False przy wyborze przycisku "Nie"
                g = messagebox.askyesnocancel("Usuwanie książki", 
                        "Czy na pewno chcesz kontynuować usuwanie książki "
                        "z bazy?")

                # Jeżeli użytkownik wciśnie "Tak" to wykona się poniższa 
                # intrukcja warunkowa
                if g == True:
                    # Otwieram baze a następnie przepisuje wszystkie wiersze 
                    # które ID jest różne od tego które zostało podane 
                    # przez użytkownika
                    otwarcie_bazy = otwarcie_bazy[otwarcie_bazy['ID'] 
                    != id_ksiazki] 
            else:
                # Jeżeli podany identyfikator książki nie istnieje w bazie 
                # danych to użytkownik dostanie powiadomienie o tym aby 
                # podać istniejący identyfikator
                messagebox.showwarning("Uwaga!",
                "Podany identyfikator nie istnieje w bazie danych książek."
                "\nProsimy o podanie istniejącego ID!")


            otwarcie_bazy.to_csv('baza.csv', index=False)
        
        def wyczysc_dane(wprowadz_id_ksiazki):
            wprowadz_id_ksiazki.delete(0, tk.END)

        #Przyciski
        tk.Button(self, bg="#D3D3D3",text="Usuń", fg="#cf0000", cursor="hand2", 
                width=40, height=3 ,font= "Times 15 bold",
                command=lambda:usuwanie_ksiazki(wprowadz_id_ksiazki)).pack()

        tk.Button(self, bg="#D3D3D3",text="Wyczyść", fg="#4700ff",
                cursor="hand2", width=40, height=3 ,font= "Times 15 bold" , 
                command=lambda:wyczysc_dane(wprowadz_id_ksiazki)).pack()

        tk.Button(self, bg="#D3D3D3",text="Wyświetl bazę po usunięciu książki", 
                cursor="hand2", width=40, height=3 ,font= "Times 15 bold",
                command= lambda: master.zmiana_okna(Wyswietlanie)).pack()

        tk.Button(self, bg="#D3D3D3",text = "Powrót do strony głównej", 
                height=3, width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Menu)).pack()


class Wyszukiwanie(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="WYSZUKAJ KSIĄŻKĘ", font="Times 35 bold", 
               width= 50, height= 0).pack(ipady=20)
        
        tk.Label(self, text="Wybierz opcje po jakiej frazie ma zostać "
        "wykonane szukanie książki",font="Times 13").pack(ipady=15)

        zmienna_wyboru = tk.StringVar()
        wybor = ("Identyfikatorze", "Tytule", "Autorze", "Roku wydania")
        zmienna_wyboru.set(wybor[0])

        menu_z_opcja = ttk.Combobox(self, values = wybor, width=20, 
                                   font = "Times 15")
        menu_z_opcja.pack(ipady=15)
        
        tk.Label(self, text="Wprowadź frazę:",font="Times 13").pack(ipady=6)
        wprowadz_fraze = tk.Entry(self, width=60)
        wprowadz_fraze.pack(ipady=15)

        def szukanie_ksiazki(menu_z_opcja, wprowadz_fraze):
            otwarcie_bazy= pandas.read_csv('baza.csv')

            # fraza_z_wyboru to zmienna która przechowuje jaka kategoria 
            # szukania została wybrana w comboboxie
            fraza_z_wyboru = menu_z_opcja.get()

            # szukana_fraza to fraza z pola entry -> czyli danych 
            # wprowadzonych przez użytkownika
            szukana_fraza = wprowadz_fraze.get()

#-------------------------------------------------------------------------------
            # szukanie książki po identyfikatorze
            if(fraza_z_wyboru == "Identyfikatorze" and szukana_fraza.isdigit()):
                # zmienna identyfikator to ID którego szukamy
                identyfikator = int(szukana_fraza) 
                pobrane_z_bazy=""

                # Zmienna która przechowuje całą kolumnę ID
                ID_z_bazy = otwarcie_bazy['ID']

                # Jeżeli podany przez użytkownika identyfikator książki 
                # istnieje  w wartościach kolumny ID to wykonają się 
                # instrukcje dla if
                if identyfikator in ID_z_bazy.values:
                    master = tk.Tk()
                    master.geometry("750x300")
                    master.title("Ekstrakt z bazy danych")
                    # przypisujemy do zmiennej wiersz/wiersze które 
                    # zawierają się pod danym identyfikatorem
                    pobrane_z_bazy = otwarcie_bazy[otwarcie_bazy['ID']== 
                                                  identyfikator]

                    tk.Label(master, text="Znaleziona książka/książki:",
                            font="Times 13").pack(ipady=5)

                    # Wyświetlanie bazy w okienku którym jest możliwość 
                    # scrollowania
                    wyswietlanie_w_okienku = scrolledtext.ScrolledText(master, 
                                             width=80, height=9)
                    wyswietlanie_w_okienku.pack()
                    wyswietlanie_w_okienku.insert(tk.INSERT, pobrane_z_bazy)

                   # Konfiguruje wyświetlanie w okienku tylko do odczytu 
                   # (read-only)
                    wyswietlanie_w_okienku.configure(state='disabled')

                     # Prycisk który zakańcza pokazywanie znalezionej książki
                    tk.Button(master,bg="#D3D3D3",text = "Zamknij", height=3, 
                     width=40, font = "Times 15 bold" , cursor="hand2", 
                     command= lambda: master.destroy()).pack()

                    master.mainloop()

                else:
                    messagebox.showwarning("Uwaga!",
                    "Podana fraza nie ma swojego odpowiednika w bazie "
                    "danych.\nSprawdź poprawność wprowadzonych danych "
                    "i spróbuj ponownie!")

#-------------------------------------------------------------------------------
            # szukanie książki po tytule
            elif(fraza_z_wyboru == "Tytule" ):
                # zmienna tytul to tytul którego szukamy
                tytul= str(szukana_fraza) 
                pobrane_z_bazy=""

                # Zmienna która przechowuje całą kolumnę tytulu
                tytul_z_bazy = otwarcie_bazy['Tytuł']

                # Jeżeli podany przez użytkownika tytul książki istnieje 
                # w wartościach kolumny tytuł to wykonają się instrukcje 
                # dla if
                if tytul in tytul_z_bazy.values:
                    master = tk.Tk()
                    master.geometry("750x300")
                    master.title("Ekstrakt z bazy danych")
                    # przypisujemy do zmiennej wiersz/wiersze które 
                    # zawierają się pod danym tytułem
                    pobrane_z_bazy = otwarcie_bazy[otwarcie_bazy['Tytuł']
                                                   == tytul]

                    tk.Label(master, text="Znaleziona książka/książki:",
                            font="Times 13").pack(ipady=5)

                    #Wyświetlanie bazy w okienku którym jest możliwość 
                    # scrollowania
                    wyswietlanie_w_okienku = scrolledtext.ScrolledText(master, 
                                            width=80, height=9)
                    wyswietlanie_w_okienku.pack()
                    wyswietlanie_w_okienku.insert(tk.INSERT, pobrane_z_bazy)

                   # Konfiguruje wyświetlanie w okienku tylko do odczytu 
                   # (read-only)
                    wyswietlanie_w_okienku.configure(state='disabled')

                    # Prycisk który zakańcza pokazywanie znalezionej książki
                    tk.Button(master,bg="#D3D3D3",text = "Zamknij", height=3, 
                     width=40, font = "Times 15 bold" , cursor="hand2", 
                     command= lambda: master.destroy()).pack()

                    master.mainloop()

                else:
                    messagebox.showwarning("Uwaga!",
                    "Podana fraza nie ma swojego odpowiednika w bazie danych."
                    "\nSprawdź poprawność wprowadzonych danych i "
                    "spróbuj ponownie!")
                    
#-------------------------------------------------------------------------------
            # szukanie książki po autorze
            elif(fraza_z_wyboru == "Autorze" ):
                # zmienna autor to autor po którym szukamy ksiazki
                autor= str(szukana_fraza) 
                pobrane_z_bazy=""

                # Zmienna która przechowuje całą kolumnę autora
                autor_z_bazy = otwarcie_bazy['Autor']

                # Jeżeli podany przez użytkownika autor książki istnieje 
                # w wartościach kolumny autor to wykonają się instrukcje
                # dla if
                if autor in autor_z_bazy.values:
                    master = tk.Tk()
                    master.geometry("750x300")
                    master.title("Ekstrakt z bazy danych")
                    # przypisujemy do zmiennej wiersz/wiersze które 
                    # zawierają się pod danym autorem
                    pobrane_z_bazy = otwarcie_bazy[otwarcie_bazy['Autor']
                                                  == autor]

                    tk.Label(master, text="Znaleziona książka/książki:",
                            font="Times 13").pack(ipady=5)

                    #Wyświetlanie bazy w okienku którym jest możliwość 
                    # scrollowania
                    wyswietlanie_w_okienku = scrolledtext.ScrolledText(master, 
                                            width=80, height=9)
                    wyswietlanie_w_okienku.pack()
                    wyswietlanie_w_okienku.insert(tk.INSERT, pobrane_z_bazy)

                   # Konfiguruje wyświetlanie w okienku tylko do odczytu 
                   # (read-only)
                    wyswietlanie_w_okienku.configure(state='disabled')

                     # Prycisk który zakańcza pokazywanie znalezionej książki
                    tk.Button(master,bg="#D3D3D3",text = "Zamknij", height=3, 
                     width=40, font = "Times 15 bold" , cursor="hand2", 
                     command= lambda: master.destroy()).pack()

                    master.mainloop()
                
                else:
                    messagebox.showwarning("Uwaga!",
                    "Podana fraza nie ma swojego odpowiednika w bazie danych."
                    "\nSprawdź poprawność wprowadzonych danych i spróbuj "
                    "ponownie!")

#-------------------------------------------------------------------------------
            # szukanie książki po roku wydania
            elif(fraza_z_wyboru == "Roku wydania" and szukana_fraza.isdigit()):
                # zmienna rok to rok wydania którego szukamy
                rok = int(szukana_fraza) 
                pobrane_z_bazy=""

                # Zmienna która przechowuje całą kolumnę rok
                rok_z_bazy = otwarcie_bazy['Rok']
            
                # Jeżeli podany przez użytkownika rok wydania książki istnieje 
                # w wartościach kolumny Rok to wykonają się instrukcje dla if
                if rok in rok_z_bazy.values:
                    master = tk.Tk()
                    master.geometry("750x300")
                    master.title("Ekstrakt z bazy danych")
                    # przypisujemy do zmiennej wiersz/wiersze które zawierają 
                    # się pod danym rokiem wydania
                    pobrane_z_bazy = otwarcie_bazy[otwarcie_bazy['Rok']== rok]

                    tk.Label(master, text="Znaleziona książka/książki:",
                            font="Times 13").pack(ipady=5)

                    #Wyświetlanie bazy w okienku którym jest możliwość 
                    # scrollowania
                    wyswietlanie_w_okienku = scrolledtext.ScrolledText(master, 
                                            width=80, height=9)
                    wyswietlanie_w_okienku.pack()
                    wyswietlanie_w_okienku.insert(tk.INSERT, pobrane_z_bazy)

                   # Konfiguruje wyświetlanie w okienku tylko do odczytu 
                   # (read-only)
                    wyswietlanie_w_okienku.configure(state='disabled')

                     # Prycisk który zakańcza pokazywanie znalezionej książki
                    tk.Button(master,bg="#D3D3D3",text = "Zamknij", height=3, 
                     width=40, font = "Times 15 bold" , cursor="hand2", 
                     command= lambda: master.destroy()).pack()

                    master.mainloop()
                
                else:
                    messagebox.showwarning("Uwaga!",
                    "Podana fraza nie ma swojego odpowiednika w bazie danych."
                    "\nSprawdź poprawność wprowadzonych danych i spróbuj "
                    "ponownie!")
            
        def wyczysc_dane(wprowadz_fraze, menu_z_opcja):
            wprowadz_fraze.delete(0, tk.END)
            menu_z_opcja.delete(0, tk.END)
        
        # Aby móc dodać dwa przyciski obok siebie tworzę nowy Frame w tym 
        # samym okienku i 
        # w tym Frame je tam umieszcze   
        top = tk.Frame(self)
        # i wyświetlam go z pozycją u góry
        top.pack(side=tk.TOP)

        #Przyciski
        # Parametr in_= pozwala umieścić widżet w innym kontenerze, o ile 
        # argument „in_” jest potomkiem rodzica
        tk.Button(self,bg="#D3D3D3", text="Szukaj", fg="#3da063",
                cursor="hand2", width=20, height=3 ,font= "Times 10 bold" , 
                command=lambda:szukanie_ksiazki(menu_z_opcja, 
                wprowadz_fraze)).pack(side=tk.LEFT, in_=top)

        tk.Button(self,bg="#D3D3D3", text="Wyczyść",fg="#4700ff",
                cursor="hand2", width=20, height=3 ,font= "Times 10 bold" , 
                command=lambda:wyczysc_dane(wprowadz_fraze, menu_z_opcja)).pack(
                    side=tk.RIGHT, in_=top)


        tk.Button(self, bg="#D3D3D3",text = "Powrót do strony głównej", 
                height=3, width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Menu)).pack()

if __name__ == "__main__":
    baza_ksiazek = Aplikacja()
    baza_ksiazek.mainloop()
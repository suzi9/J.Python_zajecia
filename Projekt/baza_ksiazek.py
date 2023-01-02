from tkinter import *
from pandas import *
from tkinter import scrolledtext
from tkinter import messagebox
import csv

class Aplikacja(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.okno = None
        self.zmiana_okna(Menu)
        # nazwa okienka
        self.title("Baza danych książek")
        # funkcja geometry() służy do ustawiania wymiarów okna Tkintera 
        self.geometry("750x600")

    def zmiana_okna(self, klasa_okna):
        nowe_okno = klasa_okna(self)

        if self.okno is not None:
            self.okno.destroy()

        self.okno = nowe_okno
        self.okno.pack()

class Menu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="BAZA DANYCH KSIĄŻEK", font="Times 35 bold", width= 50, height= 0).pack()
        Label(self, text="Wybierz jaką akcje chcesz wykonać:", font="Times 20", width= 50, height= 2).pack()

        #Przyciski
        Button(self,bg="#D3D3D3", text = "Wyświetl bazę książek", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Wyswietlanie)).pack()
        Button(self,bg="#D3D3D3", text = "Dodaj nową książke", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Dodawanie)).pack()
        Button(self,bg="#D3D3D3", text = "Usuń książke", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Usuwanie)).pack()
        # Prycisk który zakańcza pracę programu
        Button(self,bg="#D3D3D3",text = "Zamknij", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.destroy()).pack()

class Wyswietlanie(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="LISTA WSZYSTKICH KSIĄŻEK W BAZIE", font="Times 20 bold", width= 50, height= 0).pack()
        
        #Wyświetlanie bazy w okienku którym jest możliwość scrollowania
        # read_csv() i .head() pochodzą z modułu pandas
        otwarcie_bazy= read_csv('baza.csv')
        wyswietlanie_w_okienku = scrolledtext.ScrolledText(self,  width=80, height=29)
        wyswietlanie_w_okienku.pack()
        wyswietlanie_w_okienku.insert(INSERT, otwarcie_bazy)
        
        # Konfiguruje wyświetlanie w okienku tylko do odczytu (read-only)
        wyswietlanie_w_okienku.configure(state='disabled')
        
        #Przyciski
        Button(self, bg="#D3D3D3",text = "Powrót do strony głównej", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Menu)).pack()

class Dodawanie(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        Label(self, text="DODAJ NOWĄ KSIĄŻKĘ", font="Times 35 bold", width= 50, height= 0).pack()
        
        #Wpowadzanie identyfikatora
        Label(self, text="Podaj identyfikator książki",font="Times 13").pack()
        wprowadz_id = Entry(self, width=60)
        # ipady używam do ustawienia wyskości pola o wpisywania czyli entry
        wprowadz_id.pack(ipady=15)

        #Wprowadzanie tytułu
        Label(self, text="Podaj tytuł książki",font="Times 13").pack()
        wprowadz_tytul = Entry(self, width=60)
        wprowadz_tytul.pack(ipady=15)

        #Wprowadzanie autora
        Label(self, text="Podaj autora książki",font="Times 13").pack()
        wprowadz_autora = Entry(self, width=60)
        wprowadz_autora.pack(ipady=15)

        #Wprowadzanie roku
        Label(self, text="Podaj rok wydania książki",font="Times 13").pack()
        wprowadz_rok = Entry(self, width=60)
        wprowadz_rok.pack(ipady=15)
        
        def dodaj_ksiazke(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok):
            
            otwarcie_bazy= read_csv('baza.csv')

            #Pobranie identyfikaora ksiazki
            identyfikator = int(wprowadz_id.get())
            
            # Jeżeli podany identyfikator książki nie istnieje to dodamy książke do bazy
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
                zapisac_dane = DataFrame(wszystkie_dane)

                # używam escapechar i quoting aby do pliku .csv zapisywac dane bez cudzyłowów, żeby mi się poprawnie
                # baza wyświetlała
                zapisac_dane.to_csv('baza.csv', index=False, mode='a', header=False, escapechar=' ' , quoting=csv.QUOTE_NONE)

            # w przeciwnym wypadku dajemy komunikat użytkownikowi że książka o takim ID już istnieje 
            else:
                messagebox.showwarning("Uwaga!","Podany identyfikator już istnieje w bazie danych książek.\nProsimy o podanie innego ID!")

            
        
        # Funkcja do czysczenia pól entry -> tam gdzie się wrowadza dane
        def wyczysc_wprowadzone_dane(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok):
            wprowadz_id.delete(0, END)
            wprowadz_tytul.delete(0, END)
            wprowadz_autora.delete(0, END)
            wprowadz_rok.delete(0, END)


        # Aby móc dodać dwa przyciski obok siebie tworzę nowy Frame w tym samym okienku i w tym Frame je tam umieszcze   
        top = Frame(self)
        # i wyświetlam go z pozycją u góry
        top.pack(side=TOP)

        #Przyciski
        # Parametr in_= pozwala umieścić widżet w innym kontenerze, o ile argument „in_” jest potomkiem rodzica
        Button(self,bg="#D3D3D3", text="Zapisz", fg="#3da063",cursor="hand2", width=20, height=3 ,font= "Times 10 bold" , command=lambda:dodaj_ksiazke(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok)).pack(side=LEFT, in_=top)
        Button(self,bg="#D3D3D3", text="Wyczyść",fg="#4700ff",cursor="hand2" , width=20, height=3 ,font= "Times 10 bold" , command=lambda:wyczysc_wprowadzone_dane(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok)).pack(side=RIGHT, in_=top)
        Button(self,bg="#D3D3D3", text = "Powrót do strony głównej", height=4, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Menu)).pack()

class Usuwanie(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="USUŃ KSIĄŻKĘ", font="Times 35 bold", width= 50, height= 0).pack()
        Label(self, text="Wprowadz ID książki którą chcesz usunąć",font="Times 13").pack()

        wprowadz_id_ksiazki = Entry(self, width=60)
        # ipady używam do ustawienia wyskości pola o wpisywania czyli entry
        wprowadz_id_ksiazki.pack(ipady=15)

        def usuwanie_ksiazki(wprowadz_id_ksiazki):
            #Pobranie identyfikaora ksiazki
            identyfikator = wprowadz_id_ksiazki.get()
            if identyfikator.isnumeric():
                id_ksiazki = int(identyfikator)
            
            otwarcie_bazy= read_csv('baza.csv')
            
            # Zmienna która przechowuje całą kolumnę ID
            identyfikator = otwarcie_bazy['ID']
            
            # Jeżeli podany przez użytkownika identyfikator książki istnieje w wartościach kolumny ID to wykonają się instrukcje dla if
            if id_ksiazki in identyfikator.values:
                # Wiadomość będzie nam zwracać wartość True jeśli użytkownik kliknie "Tak" i wartość False przy
                # wyborze przycisku "Nie"
                g = messagebox.askyesnocancel("Usuwanie książki", "Czy na pewno chcesz kontynuować usuwanie książki z bazy?")
                
                # Jeżeli użytkownik wciśnie "Tak" to wykona się poniższa intrukcja warunkowa
                if g == True:
                    # Otwieram baze a następnie przepisuje wszystkie wiersze które ID 
                    # jest różne od tego które zostało podane przez użytkownika
                    otwarcie_bazy = otwarcie_bazy[otwarcie_bazy['ID'] != id_ksiazki] 
            else:
                # Jeżeli podany identyfikator książki nie istnieje w bazie danych to użytkownik dostanie powiadomienie
                # o tym aby podać istniejący identyfikator
                messagebox.showwarning("Uwaga!","Podany identyfikator nie istnieje w bazie danych książek.\nProsimy o podanie istniejącego ID!")


            otwarcie_bazy.to_csv('baza.csv', index=False)
        
        def wyczysc_wprowadzone_dane(wprowadz_id_ksiazki):
            wprowadz_id_ksiazki.delete(0, END)
            
        #Przyciski
        Button(self, bg="#D3D3D3",text="Usuń", fg="#cf0000", cursor="hand2", width=40, height=3 ,font= "Times 15 bold", command=lambda:usuwanie_ksiazki(wprowadz_id_ksiazki)).pack()
        Button(self, bg="#D3D3D3",text="Wyczyść", fg="#4700ff",cursor="hand2" , width=40, height=3 ,font= "Times 15 bold" , command=lambda:wyczysc_wprowadzone_dane(wprowadz_id_ksiazki)).pack()
        Button(self, bg="#D3D3D3",text="Wyświetl bazę po usunięciu książki", cursor="hand2", width=40, height=3 ,font= "Times 15 bold",command= lambda: master.zmiana_okna(Wyswietlanie)).pack()
        Button(self, bg="#D3D3D3",text = "Powrót do strony głównej", height=3, width=40, font = "Times 15 bold" , cursor="hand2", command= lambda: master.zmiana_okna(Menu)).pack()

if __name__ == "__main__":
    baza_ksiazek = Aplikacja()
    baza_ksiazek.mainloop()
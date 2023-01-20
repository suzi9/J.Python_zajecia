# Projekt zaliczeniowy - Baza danych książek 

## *Celem projektu jest stworzenie bazy danych za pomocą modułu Tkinter.*

## Jak uruchomić program?

Aby uruchomić program, wystarczy uruchomić plik baza_ksiazek.py będąc w głównym folderze z plikami.

## Użytkowanie programu:

- Przy uruchomieniu programu użytkownika powita Menu Główne bazy danych. Służy ono do
  przemieszczania się pomiędzy różnymi funkcjami, którymi ta apliakcja udostępnia.

- Pierwszą z góry opcją jest "Wyświetl baze książek". Ta opcja wyświetla użytkownikowi
  całą bazę książek jaka istnieje. Dane wyświetlają się kolejno: \
  **pozycja** - czyli liczby od 0 do n, gdzie n to dowolna liczba całkowita dodatnia \
  **ID** - kolumna zawierająca wszytskie unikalne identyfikatory dla każdej 
    książki z osobna w bazie danych \
  **Tytuł** - kolumna zawierająca tytuły wszystkich książek \
  **Autor** - kolumna zawierająca autorów wszystkich książek \
  **Rok** - kolumna zawierająca rok wydania każdej z książek \
  Warto wspomnieć iż jeżeli baza jest bardzo rozległa, istnieje możliwość 
  przesuwania(scrollowania) bazy danych w dół. Natomiast ostatni przycisk 
  "Powrót do strony głównej", przełącza użytkownika do Menu
  Głównego w celu podjęcia dodatkowych akcji.

- Drugą opcją jest "Dodaj nową książkę", ta opcja jak sama nazwa sugeruje służy
  do dodania nowej książki do bazy danych użytkownika. Użytkownik samodzielnie 
  wprowadza wszystkie dane w pola do tego przeznaczone a następnie korzysta z
  przycisku "Zapisz" jeżeli chce zapisać książkę w bazie. Natomiast jeżeli poda 
  książkę o już istniejącym ID, to użytkownik zostanie o tym powiadomiony przez
  pojawiający się komunikat. I dopóki użytkownik nie wprowadzi ID innego od tych 
  aktualnych, to książka nie zostanie zapisana.
  Jest jeszcze przycisk "Wyczyść", mianowicie służy on do wyczyszczenia pola 
  które służy do wprowadzania danych. Dzięki temu użytkownik nie jest zmuszony
  do wykonywania czyszczenia pola ręcznie, jeżeli chce podać nowe dane.
  Ostatni przycisk "Powrót do strony głównej", przełącza użytkownika do Menu
  Głównego w celu podjęcia dodatkowych akcji.

- Trzecią opcją jest "Usuń książkę", która służy do usunięcia książki z bazy
  danych użytkownika. Użytkownik ma do dyspozycji 4 różne przyciski, pierwszy 
  "Usuń" służy do usunięcia książki o tym identyfikatorze jaki podał użytownik.
  Natiomiast zanim to nastąpi, najpierw pojawia się komunikat pytający użytkownika 
  ponownie czy na pewno wyraża chęć usunięcia książki. Jeżeli zostanie wybrana 
  opcja "Nie" lub "Anuluj", operacja usuwania zostanie anulowana. Natomiast
  przy wybraniu przez użytkownika opcji "Tak', operacja usuwania się powiedzie.
  Ten pojawiający się komunikat ma służyć na wypadek jeśli użytkownik nie celowo 
  wcisnąłby przycik "Usuń", wtedy zapobiega się przypadkowemu usunięciu danych.
  Ogólnie jeżeli użytkownik podjłąby próbę usunięcia książki o ID którego
  nie ma w bazie danych to również dostanie on komunikat w postaci pojawiącego
  się komunikatu z wiadomośćią.
  Drugi przycisk "Wyczyść" służy do wyczyszenia pola do wprowazania danych
  przez użytkownika.
  Trzeci przycisk "Wyświetl bazę po usunięciu książki" służy do 
  wyświetlenia książki po operacji usuwania.
  Czwarty przycisk "Powrót do strony głównej", przełącza użytkownika do Menu
  Głównego w celu podjęcia dodatkowych akcji.

- Czwartą opcją jest "Zamknij", która służy do zamknięcia aplikacji.

## Poprawnie wyświetlający się interfejs programu
Menu główne
![image info](./interfejs/1.png)

OPCJA: Wyświetl bazę książek
![image info](./interfejs/2.png)

OPCJA: Dodaj nową książkę
![image info](./interfejs/3.png)

OPCJA: Usuń książkę
![image info](./interfejs/4.png)

OPCJA: Znajdź ksiązkę
![image info](./interfejs/5.png)

Po wyszukaniu według dowolnej opcji, pojawia się okienko ze znalezionymi książkami
![image info](./interfejs/6.png)

## Działanie programu - zwięzłe omówienie kodu

Bazą przechowującą wszystkie dane w tym programie jest plik
baza.csv .
Pierwszą widoczną klasą w kodzie jest klasa o nazwie "Aplikacja".
```python
class Aplikacja(tk.Tk):
```
Zawiera ona konstruktor, który inicjalizuje nam powstanie obiektu Tk.
Czyli okienka z modułu Tkinter.
```python
def __init__(self):
```
Oraz klasa zawiera poniższą funkcję która odpowiada za niszczenie bieżącej 
ramki(Frame) i zastępuje go nową ramką. Korzystając z tej funkcji
daje nam to możliwość przemieszczania się pomiędzy różnymi ramkami które 
zostały stworzone jako inne klasy w tym programie.
```python
def zmiana_okna(self, klasa_okna):
```
---

Druga klasa jest o nazwie "Menu". W swoim konstruktorze zawiera głównie
widżety Label i Button. Gdzie Label służy do wyświetlania tekstu na
ekranie. A Button jest widżetem który zawiera tekst na sobie i wywołuje 
daną akcję po przyciśnięciu, poprzez odwołanie się do konkretnej funkcji.
```python
class Menu(tk.Frame):
```
Poniżej można zauważyć że w klasie Menu głównie odwołuje się do funkcji
zmieniającej ramke(Frame), którą omówiłam powyżej. 
Przykład z programu:
```python
tk.Button(self,bg="#D3D3D3", text = "Wyświetl bazę książek", height=3, 
                width=40, font = "Times 15 bold" , cursor="hand2", 
                command= lambda: master.zmiana_okna(Wyswietlanie)).pack()
```
---

Trzecia klasa o nazwie "Wyświetlanie" służy do wyświetlania zawartości
bazy danych książek w okienku Tkintera. 
```python
class Wyswietlanie(tk.Frame):
```
Ogólnie ta baza książek wyświetlana jest w widżetie scrolledtext, co daje nam 
możliwość wygodnego poruszania się góra-dół po bazie danych, jeżeli pozycji 
będzie więcej niż program jest w stanie wyświetlić.
```python
wyswietlanie_w_okienku = scrolledtext.ScrolledText(self,  width=80, height=29)
```
W tej klasie dużą uwagę przyłożyłam również do tego, aby użytkownik nie był wstanie 
zmienić żadnych danych podczas wyświetlania bazy. Zabezpieczyłam to za pomocą funkcji
.configure gdzie jako argument podałam że stan ma zostać disabled czyli wyłączony.
Co sprawia że wtedy baza w widżecie scrolledtex wyświetla się wyłącznie do odczytu.
```python
wyswietlanie_w_okienku.configure(state='disabled')
```
---

Czwarta klasa o nazwie "Dodawanie" służy do dodawania książek przez użytkownika
do bazy danych.
```python
class Dodawanie(tk.Frame):
```
Mianowicie użytkownik wprowadza dane w odpowiednie pola widżetu Entry, który właśnie
pozwala wprowadzić pojedńczy wiersz tekstu. Od użytkownika wymagane jest wypełenienie
pól ID, Tytuł, Autor i Rok. Następnie wprowadzone przez użytkownika dane, są pobierane 
z pól widżetu Entry za pomocą funkcji .get(). Przykład:
```python
tytul = wprowadz_tytul.get()
```
Co prawda pobranie znaków następuje dopiero wtedy gdy użytkownik kliknął przycisk "Zapisz".
Ponieważ po przyciśnięciu przycisku "Zapisz "wywołuje się następująca funkcja:
```python
def dodaj_ksiazke(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok):
```
I w tej funkcji następuje odczytanie danych z bazy, a następnie wprowadzony przez 
użytkownika identyfikator jest sprawdzany czy istnieje jego odpowiednik w bazie
danych, jeżeli nie istnieje to zapisanie książki przebiegnie pomyślnie.
I wtedy dane zostaną połączone w jeden string, gdzie słowa są odzielone przecinkami
i ten string zostanie zapisany do pliku baza.csv za pomocą funkcji .to_csv().
```python
zapisac_dane.to_csv('baza.csv', index=False, mode='a', header=False, 
                                     escapechar=' ' , quoting=csv.QUOTE_NONE)
```
W przeciwnym wypadku gdy użytkownik poda już istniejące ID, to zostanie powiadomiony 
że podany identyfikator już istnieje. Do stworzenia komunikatu użyłam widżetu messagebox.
```python
messagebox.showwarning("Uwaga!",
        "Podany identyfikator już istnieje w bazie danych książek.\nProsimy o podanie innego ID!")
```
Kiedy użytkownik wciśnie przycisk "Wyczyść", nastąpi wywołanie funkcji czyszczącej
pola do wprowadzania danych.
```python
def wyczysc_dane(wprowadz_id, wprowadz_tytul, wprowadz_autora, wprowadz_rok):
```
Ta funkcja czyści pola widżetu Entry za pomocą funkcji delete() użytej do każdego
obiektu Entry.
Przykład z programu:
```python
wprowadz_id.delete(0, tk.END)
```
---

Piąta klasa o nazwie "Usuwanie", służy do usunięcia książki z bazy danych
o podanym przez użytkownika identyfikatorze.
```python
class Usuwanie(tk.Frame):
```
Ogólnie analogicznie wykorzystuje widżet Entry, pobieranie z niego wierszy
zarówno czyszczenie jego pola tak samo jak w klasie "Dodawanie".
Większą uwagę przyłożyłam w tej klasie do funkcji która wykonuje się
po wciśnieciu przycisku "Usuń".
```python
def usuwanie_ksiazki(wprowadz_id_ksiazki):
```
Mianowicie na początku sprawdza czy ogólne podane ID istnieje w bazie danych.
Jeżeli tak, to użytkownikowi pojawia się komunikat z zapytaniem czy aby na pewno
chce usunąć książkę o podanym przez siebie ID. Na okienku mamy trzy opcje
"Tak", "Nie" lub "Anuluj". Jeżeli użytkownik wybierze "Nie" lub "Anuluj"
to książki o podanym ID nie zostanie usunięta. Natiomiast jeżeli użytkownik 
wybierze opcje "Tak" to obiekt g zostanie ustawiony na wartość True i wykona się 
reszta kodu gdzie nastąpi usunięcie książki o tym ID.
```python
g = messagebox.askyesnocancel("Usuwanie książki", 
                        "Czy na pewno chcesz kontynuować usuwanie książki z bazy?")
```
Ogólnie ma to służyć w przypadku niezdarności użytkownika, czyli przypadkowym 
wciśnięciem przycisku "Usuń". 
A jeżeli użytkownik wprowadzi nieistniejące ID to również dostanie do tego 
stosowny komunikat.

---

## Projekt napisany przy użyciu
- Python 3.10.7 
- Pandas 1.5.2
- Tkinter 8.6.10
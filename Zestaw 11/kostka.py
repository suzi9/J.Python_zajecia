import tkinter as tk
import random

master = tk.Tk()
# nazwa okienka
master.title("Rzut kostką")
# funkcja geometry() służy do ustawiania wymiarów okna Tkintera 
master.geometry("750x600")

def wynik():

    rzut = random.randint(1, 6)
    label.configure( text = rzut )
    label.pack()


tk.Button(master, text = "Rzuć kostką", height=3, width=40,font = "Times 15 bold" , 
          cursor="hand2", bg="#47e5b8",command=wynik).pack()

label=tk.Label(master, height=28, font=("arial", 300))

master.mainloop()

        




print("\nProgram ktory rysuje prostokaty lub kwadraty zbudowane z malcyh kratek\n")
szerokosc = int(input("\nPodaj szerokosc: "))
wysokosc = int(input("Podaj wysokosc: "))
linia = "+"
kreska = "|"
f = 0
y=0
nowa_linia = ""

for x in range(szerokosc):
    linia = linia + "---+"
    kreska = kreska + str("|").rjust(4)
        
nowa_linia = nowa_linia + linia

for y in range(wysokosc):
    nowa_linia =  nowa_linia + "\n"+ kreska + "\n" + linia


print(nowa_linia)


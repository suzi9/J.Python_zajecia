# Poniższy kod jest napisany poprawnie składniowo, jedyne co to można tu napisać to przypisanie
# wartości do zmiennych po prostu w nowej lini zamiast średnika używać ale mimo wszystko 
# kod działa poprawnie
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#-----------------------------------------------------------------------------

# Poniższy kod nie jest napisany poprawnie składniowo, dlatego że jak uzywamy dwuchkropków
# to ogólnie powinniśmy zacząć od nowej lini tą istrukcję warunkową i funkcje print()
# i powinniśmy zrobić poprawne wcięcie kodu (czyli 4 spacje) dla instrukcji warunkowej if i funkcji print 
# Aby kod działał można go zapisać w ten sposób:
# for i in "axby":
#     if ord(i) < 100: print (i)
#         print (i)
for i in "axby": if ord(i) < 100: print (i)

#-----------------------------------------------------------------------------

# Poniższy kod jest poprawnie składniowo
for i in "axby": print (ord(i) if ord(i) < 100 else i)

#-----------------------------------------------------------------------------

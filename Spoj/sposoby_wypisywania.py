import re

lista = [1, 3, 432, 4543]

print(*lista)  # * rozpakowuje całą tablicę

lista_stringów = ["ładne stringi", "koronkowe stringi", "czerwone stringi"]
print(", ".join(lista_stringów))

moje_osoby_do_podzielenia = "Sdew Grsg (CID:43654), Tgre Rafal Hrsf (CID:54354)"

cids = []

pattern = r"\(CID:(\d*)\)"

print(list(re.finditer(pattern, moje_osoby_do_podzielenia)))

for match in re.finditer(pattern, moje_osoby_do_podzielenia):
    print(match.group(1))

with open("tabelki.txt", "w") as tabelki:
    for match in re.finditer(pattern, moje_osoby_do_podzielenia):
        print(match.group(1), file=tabelki)

with open("imiona.txt", "w") as imiona:
    moje_osoby_do_podzielenia = moje_osoby_do_podzielenia.upper()
    moje_osoby_do_podzielenia = moje_osoby_do_podzielenia.split(sep=", ")
    for osoba in moje_osoby_do_podzielenia:
        osoba = osoba.split(sep=" ")
        osoba.pop()
        print(*osoba, file=imiona)

print("abc".replace("a", "x").replace("x", "y").replace("c", "z").upper().title())  # se moge wincyj kropków na jednym

# w jednej linijce

print(*[' '.join(osoba.split()[:-1]) for osoba in open('zrodlo.txt').read().upper().split(', ')], file=open('imiona2.txt', 'w'), sep='\n')
assert open('imiona.txt').read() == open('imiona2.txt').read()

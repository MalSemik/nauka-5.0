# Rafałek wyjaśni mi, co to jest list comprehention
from tablice_2d import wypisz_tablice
import random

zera = [0] * 10
# print(zera)
# wypisz_tablice(zera)

więcej_zer = []
for i in range(10):
    więcej_zer.append([])
    for j in range(10):
        więcej_zer[i].append(0)

# wypisz_tablice(więcej_zer)
więcej_zer = []
for i in range(4):
    więcej_zer.append([0] * 4)

# wypisz_tablice(więcej_zer)

więcej_zer = [[0] * 4] * 4  # to nie list compreh. tu mamy 4 razy ten sam rząd
więcej_zer[2][2] = 34

# wypisz_tablice(więcej_zer)

# teraz dopiero list compr

więcej_zer = [[0 for i in range(4)] for j in range(4)]
więcej_zer[2][2] = 3423
# wypisz_tablice(więcej_zer)

wiecej_a = [["a" * (i + j) for i in range(1, 4)] for j in range(25)]
wypisz_tablice(wiecej_a)

mniej_a = ["a" * i for i in range(1, 5)]

mniej_ab = [a + "b" for a in mniej_a]
print(mniej_ab)

mniej_ac = [a + "c" * (i + 1) for i, a in enumerate(mniej_a)]
print(mniej_ac)

nowa = [random.randint(0, 10) for i in range(5)]
print(nowa)

new_odds = [i for i in nowa if i % 2]  # % przyjmuje 1 - true albo 0 false
print(new_odds)

new_even = [i for i in nowa if i % 2 == 0]  # or [i for i in nowa if not i % 2]
print(new_even)


# funkcja filter
def czy_parzysta(x):
    if x % 2 == 0:
        return True
    else:
        return False


new_odds = list(filter(czy_parzysta, nowa))
print(new_odds)

quick_christmastrees = ["*"*i for i in range(100)]
wypisz_tablice(quick_christmastrees)

# TODO zrozumieć choinkę
n= 10
not_such_quick_chrismastrees = [" "*(n-i-1)+"*"*(2*i+1) for i in range(n)]
wypisz_tablice(not_such_quick_chrismastrees)
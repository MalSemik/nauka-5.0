import random


def zsumuj_tablice(tablica):
    suma = 0
    for i in range(len(tablica)):
        suma += sum(tablica[i])

    return suma


def wypisz_tablice(x):
    for k in range(len(x)):
        print(x[k])


n = 5


def stwórz_i_wypełnij_tablicę_losowymi(n):
    losowa_tablica = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            a = random.randint(1, 9)
            wiersz.append(a)
        losowa_tablica.append(wiersz)
    return losowa_tablica


losowa_tablica = stwórz_i_wypełnij_tablicę_losowymi(5)
wypisz_tablice(stwórz_i_wypełnij_tablicę_losowymi(5))


def stwórz_i_wypełnij_tablicę_zerami(n):
    tablica = []
    for i in range(n):
        tablica.append([])
        for j in range(n):
            tablica[i].append(0)
    return tablica


# tablica[2][2] = 4


# print(tablica)
# wypisz_tablice(tablica)

#
# suma = zsumuj_tablice(losowa_tablica)
# print(suma)
#
# print(zsumuj_tablice(losowa_tablica))

def utwórz_tablice_2d_przy_pomocy_list_conprehension(n):
    lista2d = [list(range(n)) for i in range(n)]
    return lista2d


def dodawanie_tablic():
    pierwsza = [1, 2, 3]
    druga = ["a", "b", "c"]
    suma = pierwsza + druga
    print(suma)


def dodawanie_elementów_tablic():
    a = [1, 2, 45]
    b = [32, 54, 65]
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    print(c)


def zsumuj_wiersze(tablica):
    suma_wierszy = []
    for i in range(len(tablica)):
        suma_wierszy.append(sum(tablica[i]))
    print(suma_wierszy)
    return suma_wierszy

def zsumuj_kolumny(tablica):
    suma_kolumn = []
    for i in range(len(tablica)):
        suma = 0
        for j in range(len(tablica)):
            suma1 = tablica[j][i]  # suma = tablica [i][j] sumuje wiersze
            suma += suma1
        suma_kolumn.append(suma)
    print(suma_kolumn)
    return suma_kolumn

def zsumuj_przekątną_od_lewej_do_prawej(tablica):
    suma_przekatnej = 0
    for i in range(len(tablica)):
        suma_przekatnej += tablica[i][i]  # suma = tablica [i][j] sumuje wiersze

    print(suma_przekatnej)
    return suma_przekatnej

def zsumuj_przekątną_od_prawej_do_lewej(tablica):
    suma_drugiej_przekatnej = 0
    for i in range(len(tablica)):
        suma_drugiej_przekatnej += tablica[i][n - i - 1]  # suma = tablica [i][j] sumuje wiersze
    print(suma_drugiej_przekatnej)
    return suma_drugiej_przekatnej

#
# # sumowanie dwuwymiarowych tabliców
# # tablica + losowa_tablica
# wynik = []
# for j in range(n):
#     wynik.append([])
#     for k in range(n):
#         wynik[j].append(tablica[j][k] + losowa_tablica[j][k])
#
# print(*wynik, sep="\n", end="\n\n", file=open("wynik.txt","a"))
# wypisz_tablice(wynik)

if __name__ == '__main__':  # dzieki temu jak zaimportuje gdzieś funkcje z tego pliku to sie nie wykona to, co jest pod ifem
    print('coś')
    # suma wierszy

    suma_wierszy = []
    for i in range(len(losowa_tablica)):
        suma_wierszy.append(sum(losowa_tablica[i]))

    print(suma_wierszy)

    suma_kolumn = []
    for i in range(len(losowa_tablica)):
        suma = 0
        for j in range(len(losowa_tablica)):
            suma1 = losowa_tablica[j][i]  # suma = losowa_tablica [i][j] sumuje wiersze
            suma += suma1
        suma_kolumn.append(suma)

    print(suma_kolumn)

    suma_przekatnej = 0
    for i in range(len(losowa_tablica)):
        suma_przekatnej += losowa_tablica[i][i]  # suma = losowa_tablica [i][j] sumuje wiersze

    print(suma_przekatnej)

    suma_drugiej_przekatnej = 0
    for i in range(len(losowa_tablica)):
        suma_drugiej_przekatnej += losowa_tablica[i][n - i - 1]  # suma = losowa_tablica [i][j] sumuje wiersze
    print(suma_drugiej_przekatnej)

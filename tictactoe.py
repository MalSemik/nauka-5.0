import random


def utwórz_plansze(n):
    plansza = []
    for i in range(n):
        plansza.append([])
        for j in range(n):
            plansza[i].append(" ")
    return plansza


def wypisanie_planszy(plansza):
    print(*plansza, sep="\n")


def wypisanie_planszy_for(plansza):
    for i in range(len(plansza)):
        print('| ', end='')
        for j in range(len(plansza)):
            print(plansza[i][j], '| ', end="")
        print()


def ruch_gracza(plansza):
    ruch_gracza = False
    while ruch_gracza == False:
        row = int(input("Podaj indeks wiersza"))
        if row > 2:
            row = int(input("Indeks nieprawidłowy. Podaj indeks wiersza"))
        column = int(input("Podaj indeks kolumny"))
        if column > 2:
            column = int(input("Indeks nieprawidłowy. Podaj indeks kolumny"))
        if plansza[row][column] == " ":
            plansza[row][column] = ("X")
            wypisanie_planszy_for(plansza)
            ruch_gracza = True
        else:
            print("To miejsce jest już zajęte, podaj inne")

    return plansza


def ruch_gracza_x(plansza):
    ruch_gracza = False
    while ruch_gracza == False:
        row = int(input("Podaj indeks wiersza graczu X "))
        if row > 2:
            row = int(input("Indeks nieprawidłowy. Podaj indeks wiersza graczu X "))
        column = int(input("Podaj indeks kolumny graczu X "))
        if column > 2:
            column = int(input("Indeks nieprawidłowy. Podaj indeks kolumny graczu X "))
        if plansza[row][column] == " ":
            plansza[row][column] = ("X")
            wypisanie_planszy_for(plansza)
            ruch_gracza = True
        else:
            print("To miejsce jest już zajęte, podaj inne graczu X ")

    return plansza


def ruch_gracza_o(plansza):
    ruch_gracza = False
    while ruch_gracza == False:
        row = int(input("Podaj indeks wiersza graczu O "))
        if row > 2:
            row = int(input("Indeks nieprawidłowy. Podaj indeks wiersza graczu O "))
        column = int(input("Podaj indeks kolumny graczu O "))
        if column > 2:
            column = int(input("Indeks nieprawidłowy. Podaj indeks kolumnygraczu O "))
        if plansza[row][column] == " ":
            plansza[row][column] = ("O")
            wypisanie_planszy_for(plansza)
            ruch_gracza = True
        else:
            print("To miejsce jest już zajęte, podaj inne graczu O ")

    return plansza


def ruch_komputera(plansza):
    ruch_komputera = False
    while ruch_komputera == False:
        row = random.randrange(0, 3)
        column = random.randrange(0, 3)
        if plansza[row][column] == " ":
            plansza[row][column] = ("O")
            print("Ruch komputera")
            wypisanie_planszy_for(plansza)
            ruch_komputera = True
    return plansza


def ruch_mondrego_komputera(plansza):
    # ruch_mondrego_komputera = False
    # while ruch_mondrego_komputera == False:
    #     row = random.randrange(0, 3)
    #     column = random.randrange(0, 3)
    #     if plansza[row][column] == " ":
    #         plansza[row][column] = ("O")
    #         print("Ruch komputera")
    #         wypisanie_planszy_for(plansza)
    #         ruch_mondrego_komputera = True
    # return plansza
    pass


def game_over(plansza):

    for i in range(len(plansza)):
        ilosc_x = plansza[i].count("X")
        ilosc_o = plansza[i].count("O")
        # ilosc_x = [i for i in plansza if i=="X"] do sprawdzenia czy zadziała
        # ilosc_o = [i for i in plansza if i=="O"]
        if ilosc_x == 3:
            print("Wygrywa X")
            return True
        elif ilosc_o == 3:
            print("Wygrywa O")
            return True
        else:
            continue

    for i in range(len(plansza)):
        ilosc_x = 0
        ilosc_o = 0
        for j in range(len(plansza)):
            if plansza[j][i] == "X":
                ilosc_x += 1
            if plansza[j][i] == "O":
                ilosc_o += 1
        if ilosc_x == 3:
            print("Wygrywa X")
            return True
        elif ilosc_o == 3:
            print("Wygrywa O")
            return True
        else:
            continue

    ilosc_x = []
    ilosc_o = []
    for i in range(len(plansza)):
        if plansza[i][i] == "X":
            ilosc_x.append(plansza[i][i])
        if plansza[i][i] == "O":
            ilosc_o.append(plansza[i][i])
        if len(ilosc_x) == 3:
            print("Wygrywa X")
            return True
        elif len(ilosc_o) == 3:
            print("Wygrywa O")
            return True
        else:
            continue

    ilosc_x = []
    ilosc_o = []
    for i in range(len(plansza)):
        if plansza[i][n - i - 1] == "X":
            ilosc_x.append(plansza[i][n - i - 1])
        if plansza[i][n - i - 1] == "O":
            ilosc_o.append(plansza[i][n - i - 1])
        if len(ilosc_x) == 3:
            print("Wygrywa X")
            return True
        elif len(ilosc_o) == 3:
            print("Wygrywa O")
            return True
        else:
            continue

    full = [i for i in plansza if i != " "]
    if len(full) == 9:
        print("Remis")
        return True

    return False


def gra_z_glupim_komputerem():
    # plansza = [
    #     ['O', ' ', 'X'],
    #     ['X', 'O', 'O'],
    #     ['X', ' ', 'O']
    # ]
    wypisanie_planszy_for(plansza)
    is_game_over = False
    while is_game_over == False:
        ruch = ruch_gracza(plansza)
        is_game_over = game_over()
        if is_game_over == True:
            break
        komputer = ruch_komputera(plansza)
        is_game_over = game_over()
    return plansza


n = 3
#plansza = utwórz_plansze(3)
plansza = [
    ['O', 'X', 'X'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
]
koniec = game_over(plansza)
assert koniec == True
#gra = gra_z_glupim_komputerem()
def gra_z_przeciwnikiem():
    # plansza = [
    #     ['O', ' ', 'X'],
    #     ['X', 'O', 'O'],
    #     ['X', ' ', 'O']
    # ]
    wypisanie_planszy_for(plansza)
    is_game_over = False
    while is_game_over == False:
        gracz1 = ruch_gracza_o(plansza)
        is_game_over = game_over()
        if is_game_over == True:
            break
        gracz2 = ruch_gracza_x(plansza)
        is_game_over = game_over()
    return plansza


# n = 3
# plansza = utwórz_plansze(3)
# gra = gra_z_przeciwnikiem()

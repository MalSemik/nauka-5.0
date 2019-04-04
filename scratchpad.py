def przeliczWaluty():
    # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
    podajWalute = input("Podaj walutę do przeliczenia:\n")
    ilosc = input("Podaj ilość PLN do przeliczenia na " + podajWalute + "\n")

    # program przelicza wybraną walutę na PLN
    if podajWalute == "eur" or podajWalute == "EUR":
        wynik = int(ilosc) * 4.2999
        print('%0.2f' % wynik)
        print(f'{wynik:0.2f}')
    elif podajWalute == "gbp" or podajWalute == "GBP":
        wynik = int(ilosc) * 5.0272
        print('%0.2f' % wynik)
    elif podajWalute == "usd" or podajWalute == "USD":
        wynik = int(ilosc) * 3.8232
        print('%0.2f' % wynik)
    elif podajWalute == "aud" or podajWalute == "AUD":
        wynik = int(ilosc) * 2.6994
        print('%0.2f' % wynik)
    else:
        print("Error: Sproboj jeszcze raz.")
        przeliczWaluty()


# przeliczWaluty()


def przeliczWaluty2():
    # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
    podajWalute = input("Podaj walutę do przeliczenia:\n")
    ilosc = input("Podaj ilość " + podajWalute + "do przeliczenia na PLN \n")

    # program przelicza wybraną walutę na PLN
    waluta1 = "eur"
    waluta2 = "gbp"
    waluta3 = "usd"
    waluta4 = "aud"
    if podajWalute.lower() == waluta1:
        wynik = int(ilosc) * 4.2999
        print('%0.2f' % wynik)
    elif podajWalute.lower() == waluta2:
        wynik = int(ilosc) * 5.0272
        print('%0.2f' % wynik)
    elif podajWalute.lower() == waluta3:
        wynik = int(ilosc) * 3.8232
        print('%0.2f' % wynik)
    elif podajWalute.lower() == waluta4:
        wynik = int(ilosc) * 2.6994
        print('%0.2f' % wynik)
    else:
        print("Error: Wybrano zla walute. Sproboj jeszcze raz.")
        przeliczWaluty2()



print('"EUR": 4.2999, "GPD": 5.0272, "USD": 3.8232, "AUD": 2.6994'.replace("\"", "").replace(", ","\n").replace(": ","="))

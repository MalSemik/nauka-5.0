# słownik kursów
kursy = {"EUR": 4.2999, "GPD": 5.0272, "USD": 3.8232, "AUD": 2.6994}


def moje_przeliczWaluty(kurs):
    # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
    podajWalute = input("Podaj walutę do przeliczenia:\n")
    while podajWalute.upper() not in kursy:
        podajWalute = input("Wybrano złą walutę, podaj jeszcze raz: ")

    czy_wczytano_poprawnie = False
    while not czy_wczytano_poprawnie:
        ilosc = input("Podaj ilość " + podajWalute + " do przeliczenia na PLN \n")
        try:
            ilosc = float(ilosc)
            czy_wczytano_poprawnie = True
        except:
            czy_wczytano_poprawnie = False

    # obliczanie
    print(f'{ kursy[podajWalute.upper()]*float(ilosc):0.2f}')


def wypisz_kursy(kursy):
    print(kursy)


def bulletproof_float_input(message):
    czy_wczytano_poprawnie = False
    while not czy_wczytano_poprawnie:
        ilosc = input(message)
        try:
            ilosc = float(ilosc)
            czy_wczytano_poprawnie = True
        except:
            czy_wczytano_poprawnie = False
    return ilosc


def input_exchange_rate(exchange_rates):
    # TODO (gjklv8) Doesn't work. Fix! 
    currency = input("Podaj walutę: ").upper()
    while currency not in exchange_rates:
        rate = bulletproof_float_input(f"Podaj kurs {currency}")
        exchange_rates[currency] = rate
    return currency, rate


def parse_float(value):  # parse - parsowanie, kiedy chcesz cos wyciągnac ze stringa
    try:
        value = float(value)
        return value
    except ValueError:
        return None


def read_exchange_rates():
    exchange_rates = {}
    with open("kursy.txt", "r") as file:
        for line in file:
            currency, rate = line.split("=")
            exchange_rates[currency] = float(rate)
    return exchange_rates


def add_exchange_rate(currency, rate):
    with open("kursy.txt", "a") as file:
        print(f"{currency}={rate}", file=file)


def menu():
    print("1. Calculate\n"
          "2. Add currency\n"
          "3. List supported currencies\n"
          "4. Exit\n")


if __name__ == '__main__':
    menu()
    actions = {"1": lambda: moje_przeliczWaluty(read_exchange_rates()),
               "2": lambda: add_exchange_rate(*input_exchange_rate(read_exchange_rates())),
               "3": lambda: print(read_exchange_rates())}
    choice = input()
    while choice != "4":
        actions[choice]()
        menu()
        choice = input()

while True:
    print("""
    MENU
    1. Dodaj osobę
    2. Odcztaj dane osoby
    3. Wyjdź """)
    choice = input("Wybierz pozycję z menu: ")

    if choice == "1":
        with open("dane_osobowe.txt", "a") as dane_osobowe:
            name = input("Podaj imię: ")
            surname = input("Podaj nazwisko: ")
            date_of_birth = input("Podaj datę urodzenia (DD.MM.YYYY): ")
            address = input("Podaj adres (miasto, ulica, numer): ")
            phone_nr = input("Podaj numer telefonu: ")
            print(name, file=dane_osobowe)
            print(surname, file=dane_osobowe)
            print(date_of_birth, file=dane_osobowe)
            print(address, file=dane_osobowe)
            print(phone_nr, file=dane_osobowe)
    elif choice == "2":
        pass
    elif choice == "3":
        break
    else:
        print("Podaj właściwy numer pozycji z menu")

    with open("dane_osobowe.txt") as dane_osobowe:
        for line in dane_osobowe:
            print(line, end="")

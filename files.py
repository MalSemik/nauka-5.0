def read_file():
    plik = open("wynik.txt", "r")
    print(plik.read())
    plik.seek(0)
    for line in plik:
        print(line, end="")
    print("słowo")
    print(plik.read())

    plik.seek(0)
    lines = plik.readlines()
    print(lines)
    plik.close()


import time


def safely_open_file():
    new_file = None
    try:
        new_file = open("new_file.txt", "w")
        new_file.write("No siema\n")
        print("no elo", file=new_file)
        new_file.flush()  # przesyła dane do pliku natychmiast, podobnie działa close,,, opróżnianie buffora
        # time.sleep(99999)
        # new_file.close()
    finally:
        if new_file:
            new_file.close()

safely_open_file()
def safely_open_file_short():
    with open("new_file.txt") as new_file:
        pass
        # tu moge robic z plikiem co chce i plik bedzie zamkniety i ogarniety i takie tam


def otwórz_głupi_plik_rafała():
    with open("train_scores.csv") as głupi_plik:
        scores = []
        for line in głupi_plik:
            line=line.split(",")
            scores.append(int(line[4]))
    print(scores)
    average = sum(scores)/len(scores)
    print(average)

    print(len(scores))
    last_100 = scores[-100:]
    new_average=sum(last_100)/100
    print(new_average)

    print(new_average-average)
otwórz_głupi_plik_rafała()
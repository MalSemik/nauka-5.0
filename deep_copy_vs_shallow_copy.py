numbers = [1, 2, 3, 4]
# płytka kopia, referencja do tego samego miejsca w pamięci. którąkolwiek zmodyfikuje, zmienia obie
numbers1 = numbers
numbers1[2] = 10

# głęboka kopia, tworzy nową listę, nowe miejsce w pamieciosze
numbers2 = numbers[:]

# 2 sposób głębokiej kopii
numbers3 = list(numbers)

print(numbers1)
print(numbers)

x = 12


def zmień_wartość():
    global x
    x = 324


zmień_wartość()
print(x)


def dodaj_do_listy(inna_lista):
    inna_lista.append("kwiatek")
    inna_lista.remove(10)


dodaj_do_listy(numbers)
print(numbers)


def dodaj_do_listy_w_troszeczke_inny_sposób(lista):
    lista = lista[:]
    lista.append("rafcio")


dodaj_do_listy_w_troszeczke_inny_sposób(numbers)
print(numbers)


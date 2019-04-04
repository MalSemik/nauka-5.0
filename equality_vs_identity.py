# w tym odcinku Rafał wyjaśni mi różnicę między equality a identity i dlaczego, apparently, muszę pisać z podkreśleniami

lista1 = ["kwiatek"]
lista2 = ["kwiatek"]

# == porównuje wszystkie elementy
if lista1 == lista2:
    print("Dwa kwiatki")

# is porównuje id
if lista1 is lista2:
    print("No nie jest")

print(id(lista1))

# is używa się głównie przy is None


if lista1 == None:
    print("Nic")

# różne ify
# if coś == coś
# if coś != coś
# if coś <= coś
# if coś >= coś

a = 5
if a > 2 and a <10:
    print("Między 2 a 10")

jest = int(input("0 czy 1"))
if jest:
    print("Jest")
    print(bool(jest))
else:
    print("ni ma")
    print(bool(jest))


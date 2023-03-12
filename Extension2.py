lista = ["jeden", "dwa", "trzy","cztery","pięć","sześć"]
print(lista)
print(lista[-1])
print(lista[2:4])
print(lista[:3])
print(lista[2:])
print(lista[-4:-1])
if "trzy" in lista:
    print("Trzy znajduje sie w ramach tej listy")
lista[0] = "zmiana pierwszego"
lista.append("ostatni")
print(lista)
lista[1:3] = ["zmiana drugiego", "zmiana trzeciego"]
print(lista)
lista[1:2] = ["zmiana wewnetrza 1", "zmiana wewnetrzna 2"]
print(lista)
lista.insert(1, "kolejna zmiana")
print(lista)
lista.remove("zmiana pierwszego")
print(lista)
lista.pop(0)
print(lista)
lista.pop(-1)
print(lista)
del lista[0]
print(lista)
print(lista[::-1])
for elementListy in range(len(lista)):
    print(elementListy, 'przerwa', end=' ')

print('')
lista.clear()
print(lista, "koniec listy")
del lista

a = "palindrom"
x = -1
for char in a:
    print(a[x], end='')
    x -= 1
print('')
print(a[::-1])
# pali = input("podaj slowo ktore sprawdzimy czy jest palindromem:")
#if pali == pali[::-1]:
#    print("tak jest palindromem")
#else:
#    print("nie, nie jest palindromem")

lista2 = ['jeden','dwa','trzy', 'Cztery']
lista3 = []
for x in lista2:
    if 'e' in x:
        lista3.append(x)
print(lista3)
lista2.sort(reverse=True)
print(lista2)

def pomniejszacz(n):
    return n - 50

numeraly = [10,40,60,120,260]
print(numeraly)
for x in numeraly:
    print(pomniejszacz(x))
lista2.sort()
print(lista2, 'test')

lista2.sort(reverse=True)
print(lista2, 'test2')
lista2.sort(key=len)
print(lista2)

lista3 = lista2 + numeraly

print(lista3)
lista2.extend(numeraly)
print(lista2)

tup = ('raz', 'dwa', 'trzy')
print(tup)

(pierwszy, drugi, trzeci) = tup
print(pierwszy)
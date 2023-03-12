slow = {
    "Imie" : "Buba",
    "Kolor" : "Bialy, Podpalany",
    "Wiek" : 3

}
print(slow)
print(slow["Wiek"])
x = slow.keys()
print(x)
slow["charakter"] = "pochmurny"

print(slow)

x = slow.values()
print(x)

x = slow.items()
print(x)

slow.update({"Imie" : "Bububa"})
print(slow)
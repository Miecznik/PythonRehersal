class Kot:
    name = ""
    race = ""
    age = 0

kot1 = Kot()
kot1.name = "Buba"
kot1.race = "Ragdoll"
kot1.age = 3

print(kot1.name)

class Ragdoll(Kot):
    race = "Ragdoll"
    def mowa(self):
        print("Moje imie to: " + self.name)

kot2 = Ragdoll()
kot2.name = "Mala"
print(kot2.race)
kot2.mowa()

class Usluga:
    def __init__(self):
        self.__cena = 1000

    def sprzedaz(self):
        print(self.__cena)

jazda = Usluga()
print(jazda.sprzedaz())
jazda.cena = 700
print(jazda.cena)


print("""kolejne zadanie

""")
class Komputer:

    def __init__(self):
        self.__maxcena = 2000

    def ujawnij(self):
        print(self.__maxcena)

    def ustal(self, price):
        self.__maxcena = price

asus = Komputer()
asus.ujawnij()
asus.maxcena = 1000
print(asus.maxcena)
asus.ujawnij()
asus.__maxcena = 1500
print(asus.__maxcena)
asus.ujawnij()
asus.ustal(1500)
asus.ujawnij()


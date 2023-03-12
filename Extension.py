import datetime


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
        print("Moja rasa to: " + self.race)

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

class Wielodziedzicznosc(Komputer,Ragdoll):
    pass

testowy1 = Wielodziedzicznosc()


print(testowy1.name)

testowy1.name = "Łobuz"

print(testowy1.name)
print(testowy1.race)

class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y= y

    def __str__(self):
        return "({x},{y})".format(x=self.x,y=self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Punkt(x, y)

punkt1 = Punkt(x=2, y=5)
print(punkt1)
punkt2 = Punkt(x=4, y=8)
print(punkt2)

print(punkt2 + punkt1)

data1 = datetime.datetime.now()
print(data1.__str__())
print(data1.__repr__())
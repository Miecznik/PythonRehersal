class Pole(object):
    def __init__(self, wysokosc, szerokosc, zajecie=None):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.pozycja = wysokosc, szerokosc
        self.zajecie = zajecie

    def zajecie(self):
        if self.zajecie == True:
            return True
        else:
            return False
    def zajetePole(self):
        if self.zajecie != None:
            return self.szach.kolor
        else:
            return False

class Szachownica:
    def __init__(self):
        pola = []
        szerokosc = [1,2,3,4,5,6,7,8]
        wysokosc = [1,2,3,4,5,6,7,8]

        for litera in wysokosc:
            for numer in szerokosc:
                pola.append(Pole(litera, numer, None))

        self.pola = pola
    def setup(self, pieces):
        for pole in self.pola:
            for szach in pieces:
                if pole.pozycja == szach.obecnaPozycja:
                    pole.szach = szach
                    szach.obecnaPozycja = pole



    def pustePola(self):
        pustePola = []
        for pole in self.pola:
            if pole.zajecie == None:
                pustePola.append(self.pozycja)
        return pustePola

class Szach(object):
    def __init__(self, kolor, obecnaPozycja):
        self.kolor = kolor
        self.obecnaPozycja = obecnaPozycja
        self.wysokosc = obecnaPozycja[0]
        self.szerokosc = obecnaPozycja[1]
        self.mozliweRuchy = []

    def ruch(self, szachownica, obecnaPozycja, x, y, repeat = None):
        self.szachownica = szachownica
        for pole in szachownica.pola:
            if pole.pozycja == (obecnaPozycja.wysokosc + x, obecnaPozycja.szerokosc + y) and pole.zajecie():
                self.mozliweRuchy.append(pole.pozycja)
                if repeat == True:
                    return self.ruch(szachownica,obecnaPozycja,x,y)
            elif pole.pole.pozycja == (obecnaPozycja.wysokosc + x, obecnaPozycja.szerokosc + y) and pole.zajecie() != szach.kolor:
                self.mozliweRuchy.append(pole.pozycja)

    def print_ruch(self, nazwaPiona):
        for ruch in self.mozliweRuchy:
            format = nazwaPiona + " w " + self.wysokosc + " " + self.szerokosc + " może poruszyc sie na: " + str(ruch[1]) + ">"
            print(format)

class Pion(Szach):
    def mozliwe_ruchy(self,szachownica,obecnePole):
        if self.kolor == "Bialy":
            gora = [self.wysokosc + 1,self.szerokosc]
            dwagora = [self.wysokosc + 2, self.szerokosc]
            goralewo = [self.wysokosc + 1, self.szerokosc - 1]
            goraprawo = [self.wysokosc + 1, self.szerokosc + 1]

        if self.kolor == "Bialy":
            gora = [self.wysokosc - 1,self.szerokosc]
            dwagora = [self.wysokosc - 2, self.szerokosc]
            goralewo = [self.wysokosc - 1, self.szerokosc - 1]
            goraprawo = [self.wysokosc - 1, self.szerokosc + 1]

        for pole in szachownica.pola:
            if pole.pozycja == gora and pole.zajecie():
                gora_pozycja = pole.pozycja
                self.mozliweRuchy.append(gora_pozycja)

            if pole.pozycja == dwagora and pole.zajecie():
                dwagora_pozycja = pole.pozycja
                self.mozliweRuchy.append(dwagora_pozycja)

            if (pole.pozycja == goralewo) and ((pole.zajetePole() != False)) and (pole.zajetePole() != self.kolor):
                self.mozliweRuchy.append(pole.pozycja)

            if (pole.pozycja == goraprawo) and ((pole.zajetePole() != False)) and (pole.zajetePole() != self.kolor):
                self.mozliweRuchy.append(pole.pozycja)

        self.print_ruch("Pion")


def grajSzachy(konfiguracja, gracz):
    plansza = Szachownica()
    plansza.setup(konfiguracja)

    for szach in konfiguracja:
        if szach.kolor == gracz:
            szach.mozliweRuchy(plansza, szach.obecnaPozycja)

def main():
    bialyGracz=[
        Pion("Bialy", [1,2]),
        Pion("Bialy", [2, 2]),
        Pion("Bialy", [3, 2]),
        Pion("Bialy", [4, 2]),
        Pion("Bialy", [5, 2]),
        Pion("Bialy", [6, 2]),
        Pion("Bialy", [7, 2]),
        Pion("Bialy", [8, 2])

    ]
    for szach in bialyGracz:
        szach.kolor = "Bialy"

    czarnyGracz=[
        Pion("Czarny", [1, 7]),
        Pion("Czarny", [2, 7]),
        Pion("Czarny", [3, 7]),
        Pion("Czarny", [4, 7]),
        Pion("Czarny", [5, 7]),
        Pion("Czarny", [6, 7]),
        Pion("Czarny", [7, 7]),
        Pion("Czarny", [8, 7])

    ]

    for szach in czarnyGracz:
        szach.kolor = "Czarny"

    initialState = bialyGracz + czarnyGracz
    gracz = "Bialy"
    grajSzachy(initialState, gracz)

test1 = Szachownica()
print(str(test1.pola))

main()


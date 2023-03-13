class Pole(object):
    def __init__(self, wysokosc, szerokosc, zajecie = None):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.pozycja = wysokosc, szerokosc
        self.zajecie = zajecie
    def zajecie(self):
        if self.zajecie() == True:
            return True
        else:
            return False

class Szachownica:
    def __init__(self):
        pola = ()
        literal = [1,2,3,4,5,6,7,8]
        numeral = ["A","B","C","D","E","F","G","H"]



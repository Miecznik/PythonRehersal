class Zwierze:
    def __init__(self):
        self.Zwierze = "Zwierze"
    def ustal(self, nazwa):
        self.Zwierze = nazwa
    def nazwij(self):
        print(self.Zwierze)

pies = Zwierze()
pies.ustal("Burek")
pies.nazwij()
class Piesel(Zwierze):

    def __init__(self, imiePiesela):
        self.Piesel = imiePiesela
        super().__init__()
    def szczekaj(self):
        print(self.Zwierze, " nazywa sie ", self.Piesel)

test1 = Piesel("burek")
test1.szczekaj()

print(test1.__dir__())
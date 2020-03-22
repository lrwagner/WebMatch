class Bankaccount:

    def __init__(self, name, kontonummer):
        self.name = name
        self.kontonummer = kontonummer
        self.betrag= 100
    
    def kontostand(self):
        print(self.kontostand)
    

test = Bankaccount(name='david', kontonummer=85684)

test.kontostand()

print(test.name)
print(test.kontonummer)
print(test.konostand)
test.kontostand = 10000
print(test.konostand)
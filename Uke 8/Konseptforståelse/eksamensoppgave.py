class Barnehage:
    def __init__(self, barn):
        self._barn = barn
    def bursdag(self):
        self._barn.bursdag()
    def bytte(self, nytt_barn):
        self._barn = nytt_barn
class Person:
    def __init__(self, alder):
        self._alder = alder
    def bursdag(self):
        self._alder += 1
    def hent_alder(self):
        return self._alder
per = Person(2)
palle = Person(5)
maurtua = Barnehage(per)
per.bursdag()
maurtua.bursdag()
print("A:", per.hent_alder())
maurtua.bytte(palle)
palle.bursdag()
print("B:", per.hent_alder())
print("C:", palle.hent_alder())
maurtua.bytte(Person(1))
print("D:", palle.hent_alder())

#Oppgave 2a: Hva skrives ut i linja som inkluderer "A:" i koden over?
#Oppgave 2b: Hva skrives ut i linja som inkluderer "B:" i koden over?
#Oppgave 2c: Hva skrives ut i linja som inkluderer "C:" i koden over?
#Oppgave 2d: Hva skrives ut i linja som inkluderer "D:" i koden over?

class Tall:
    def __init__(self, a):
        self._a = a
    def m1(self, c):
        self._a = self._a + c
    def m2(self):
        self._a = self._a * 2
    def m3(self):
        return self._a + 10
t1 = Tall(5)
t2 = Tall(2)
t1. m2()
t2.m1( t1.m3() )
print( t2.m3() )

#Hva printes ut når følgende kode kjøres?



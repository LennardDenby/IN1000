class Person:
    def __init__(self, navn: str, alder: int):
        self._navn = navn
        self._alder = alder
        self._hobbyer: list[Hobby] = []
    
    def leggTilHobby(self, hobby: "Hobby"):
        self._hobbyer.append(hobby)
    
    def skrivUtHobbyer(self):
        for hobby in self._hobbyer:
            print(hobby.hentHobbyNavn())

class Hobby:
    def __init__(self, navn: str):
        self._hobbyNavn = navn
    
    def hentHobbyNavn(self):
        return self._hobbyNavn

def legg_til_2(tall: int):
    return tall*2

def main():
    p1 = Person("Ola", 18)
    h1 = Hobby("Fotball")
    
    p1.leggTilHobby(h1)
    
    print(legg_til_2("streng"))
    
main()
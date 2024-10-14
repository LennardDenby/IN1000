class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
    
    def hent_navn(self):
        return self._navn
    
    def __str__(self):
        return f"Navn:{self._navn}, alder: {self._alder}"
    
    def __eq__(self, annetObjekt):
        return self._navn == annetObjekt._navn and self._alder == annetObjekt._alder
     
def main():
    p1 = Person("Ola", 18)
    p2 = Person("Ola", 18)
    
    print(p1)
    print(p2)
    print(p1==p2)
    
main()


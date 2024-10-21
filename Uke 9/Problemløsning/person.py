from gruppe import Gruppe

class Person:
    def __init__(self, alder, navn):
        self._alder = alder
        self._navn = navn
        self._hobbyer = []
        self._gruppe = None
    
    def legg_til_hobby(self, hobby):
        self._hobbyer.append(hobby)
    
    def legg_til_gruppe(self, gruppe):
        self._gruppe = gruppe
    
    def print_gruppe(self):
        print(f"{self._navn} er i gruppe: {self._gruppe.hent_navn()}")
    
    def lag_ny_gruppe(self, navn):
        nyGruppe = Gruppe(navn)
    
    def __str__(self):
        output = f"navn={self._navn},alder={self._alder},hobbyer="
        for hobby in self._hobbyer:
            output += hobby + ", "
        return output


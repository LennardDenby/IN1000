class Gruppe:
    def __init__(self, navn: str, filnavn: str):
        self._navn = navn
        self._personer = []
        self._les_fra_fil(filnavn)
    
    def _les_fra_fil(self, filnavn: str) -> None:
        fil = open(filnavn)
        for linje in fil:
            self._personer.append(linje.strip())
    
    def hent_personer(self) -> list[str]:
        return self._personer

g1 = Gruppe("gruppe 1", "personer.txt")
print(g1.hent_personer())
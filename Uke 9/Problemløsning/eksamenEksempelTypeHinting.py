class Gruppe:
    def __init__(self, krav: list[str]):
        self._krav = krav
        self._liste = []
    
    def legg_til_person(self, personer: list[str]) -> None:
        self._liste += personer
        
    def hent_personer(self) -> list[str]:
        return self._liste
    
    def hent_krav(self) -> list[str]:
        return self._krav

class Rom:
    def __init__(self, antSenger: int, fasiliteter: list[str]):
        self._antSenger = antSenger
        self._fasiliteter = fasiliteter
    
    def resever(self, gjester: list[str]) -> None:
        pass
    
    def hentAntSenger(self) -> int:
        return self._antSenger


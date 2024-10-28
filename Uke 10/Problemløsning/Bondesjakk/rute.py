from spiller import Spiller

class Rute:
    def __init__(self):
        self._tilhorer = None
    
    def plasser_brikke(self, spiller: Spiller) -> None:
        self._tilhorer = spiller
    
    def er_opptatt(self) -> bool:
        return self._tilhorer != None
    
    def hent_brikkeeier(self) -> Spiller:
        return self._tilhorer

    def __str__(self):
        if self._tilhorer:
            return self._tilhorer.hent_symbol()
        return "_"
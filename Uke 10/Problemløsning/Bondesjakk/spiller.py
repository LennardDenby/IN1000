class Spiller:
    def __init__(self, symbol: str):
        self._symbol = symbol
    
    def hent_symbol(self) -> str:
        return self._symbol
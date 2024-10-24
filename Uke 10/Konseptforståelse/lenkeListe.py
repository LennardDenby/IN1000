class Node:
    def __init__(self, verdi):
        self._verdi = verdi
        self._neste = None
    
    def hent_verdi(self):
        return self._verdi
    
    def hent_neste(self):
        return self._neste
    
    def set_neste(self, annen):
        self._neste = annen
        

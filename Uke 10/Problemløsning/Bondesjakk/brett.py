from rute import Rute
from spiller import Spiller

class Brett:
    def __init__(self):
        self._lag_brett()
        self._spiller1 = None
        self._spiller2 = None
        
    def _lag_brett(self) -> None:
        self._brett = []
        for _ in range(3):
            liste = [Rute(), Rute(), Rute()]
            self._brett.append(liste)
    
    def legg_til_spiller(self, symbol: str) -> None:
        if not self._spiller1:
            self._spiller1 = Spiller(symbol)
        elif not self._spiller2:
            self._spiller2 = Spiller(symbol)
        else:
            print("Det eksisterer allerede 2 spillere")
    
    def plasser_brikke(self, spiller: Spiller, x: int, y: int):
        rute = self._brett[x][y]
        
        if rute.er_opptatt():
            print("ruten er opptatt")
        else:
            rute.plasser_brikke(spiller)
    
    def _sjekk_vinner(self, liste: list[Rute]):
        return liste[0] == liste[1] and liste[0] == liste[2]
    
    def sjekk_vinner(self):
        for i in range(3):
            rad = self._brett[i]
            kolonne = [self._brett[0][i], self._brett[1][i], self._brett[2][i]]
            
            if self._sjekk_vinner(rad):
                return str(rad[0])
            if self._sjekk_vinner(kolonne):
                return str(kolonne[0])
        
        diag1 = [self._brett[0][0], self._brett[1][1], self._brett[2][2]]
        diag2 = [self._brett[0][2], self._brett[1][1], self._brett[2][0]]
        
        if self._sjekk_vinner(diag1):
            return str(diag1[0])
        if self._sjekk_vinner(diag2):
            return str(diag2[0])
        
        return None
    
    def print_brett(self):
        for rad in self._brett:
            print(rad[0], rad[1], rad[2])
    
    def spill(self):
        if not self._spiller1 or not self._spiller2:
            print("Ikke nok spillere")
            return
        
        fortsett = True
        antBrikker = 0
        
        while fortsett:
            self.print_brett()
            print(f"{self._spiller1.hent_symbol()} sin tur.")
            if antBrikker == 9:
                print("Ingen vant :(")
                return
            
            inp = input("Skriv inn kordinater: ")
            data = inp.split(" ")
            x = int(data[0])
            y = int(data[1])
            
            if 0 < x and x > 2:
                print("Velg en gyldig rute")
            elif 0 < y and y > 2: 
                print("Velg en gyldig rute")
            else:
                rute = self._brett[x][y]
                if not rute.er_opptatt():
                    self.plasser_brikke(self._spiller1, x, y)
                    antBrikker += 1
                    
                    self._spiller1, self._spiller2 = self._spiller2, self._spiller1
                    
                    vinner = self.sjekk_vinner()
                    
                    if vinner:
                        print(f"{vinner} vant!")
                        fortsett = False
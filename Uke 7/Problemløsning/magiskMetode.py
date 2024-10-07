#Dette kommer i uke 8

class Menneske:
    def __init__(self, hoyde, navn, aar):
        self._hoyde = hoyde
        self._navn = navn
        self._aar = aar
    
    def hentNavn(self):
        return self._navn

    def __str__(self):
        return self._navn
    
    def __eq__(self, andre):
        return self._navn == andre._navn
    
def main():
    m1 = Menneske(180, "Ole", 2004)
    m2 = Menneske(190, "Ole", 2005)
    
    print(m1 == m2)
    

if __name__ == '__main__':
    main()
class Person:
    def __init__(self, navn, alder, hoyde, vekt):
        self._navn = navn
        self._alder = alder
        self._hoyde = hoyde
        self._vekt = vekt

    def endre_navn(self, nytt_navn):
        self._navn = nytt_navn
    
    def hent_hoyde(self):
        return self._hoyde
    
    def skriv_ut_hilsen(self):
        print(f"Hei jeg heter {self._navn} og er {self._alder} år gammel.")
    
    def feire_bursdag(self):
        self._alder += 1
        print(f"Gratulerer med dagen {self._navn}, du er nå {self._alder} år gammel")
        
        if self._alder < 18:
            self._hoyde += 2
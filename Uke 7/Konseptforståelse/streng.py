class Streng:
    def __init__(self, verdi):
        self._verdi = verdi
    
    def count(self, bokstav):
        total = 0
        
        for char in self._verdi:
            if char == bokstav:
                total += 1
            
        return total

def hovedprogram():
    s1 = Streng("abcaa")
    print(s1.count("a"))

hovedprogram()
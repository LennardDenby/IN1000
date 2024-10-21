class Gruppe:
    def __init__(self, navn):
        self._navn = navn
        self._personer = []
    
    def legg_til_person(self, person):
        self._personer.append(person)
    
    def legg_til_hobbyer(self, hobby):
        for person in self._personer:
            person.legg_til_hobby(hobby)
    
    def hent_navn(self):
        return self._navn
    
    def __str__(self):
        output = ""
        for person in self._personer:
            output += str(person)+"\n"
        return output

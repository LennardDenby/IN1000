from person import Person
from gruppe import Gruppe

def hovedprogram():
    p1 = Person(18, "Ola")
    p2 = Person(20, "Martin")
    
    g1 = Gruppe("Gruppe 1")
    
    g1.legg_til_person(p1)
    g1.legg_til_person(p2)
    
    p1.legg_til_gruppe(g1)
    p2.legg_til_gruppe(g1)
    
    g1.legg_til_hobbyer("Fotball")
    
    p1.print_gruppe()

hovedprogram()

from person import Person

def hovedprogram():
    ole = Person("Ole", 15, 180, 80)
    
    ole.skriv_ut_hilsen()
    ole.feire_bursdag()
    print(ole.hent_hoyde())
    
hovedprogram()
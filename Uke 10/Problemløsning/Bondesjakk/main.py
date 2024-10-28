from brett import Brett

def hovedprogram():
    brett = Brett()
    brett.legg_til_spiller("X")
    brett.legg_til_spiller("O")
    
    print(brett._spiller1.hent_symbol())
    print(brett._spiller2.hent_symbol())
    
    brett.spill()
    
hovedprogram()
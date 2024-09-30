def forkort_lagliste(lagliste):
    return list(set(lagliste))
    

def hovedprogram():
    assert forkort_lagliste(["Brann", "Molde", "Brann", "Molde"]) == ["Brann", "Molde"]
    
hovedprogram()
def bygg_samling(antall_rader, antall_kolonner):
    samling = []


    while antall_rader > 0:
        rad = []


        for kolonnenr in range(antall_kolonner):
            rad.append(kolonnenr)
       
        samling.append(rad)
        antall_rader -= 1


    return samling


def hovedprogram():
    samling = bygg_samling(7, 5)
    


hovedprogram()
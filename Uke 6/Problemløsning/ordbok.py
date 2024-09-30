def ord_i_ordbok(setning):
    liste = setning.split()
    ordbok = {}
    
    for ord in liste:
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1
    
    return ordbok

print(ord_i_ordbok("Hei på deg deg"))


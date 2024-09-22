liste = [6, 3, 2, 8, 11]

for tall in liste:
    print(tall)
    
def prosedyre(liste):
    for tall in liste:
        print(liste)

#Argumentet vil være listen vi definnerer i linje 1
#[6, 3, 2, 8, 11] vil være verdien til parameteret

def finnMinste(liste):
    minste = liste[0]
    
    for tall in liste:
        if tall < minste:
            minste = tall
    
    print(f"Minste tallet er: {minste}")

finnMinste(liste)

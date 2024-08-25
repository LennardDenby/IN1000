#Eksempel 1:

alder = 25
tidspunkt = "kveld"

if alder < 18:
    if tidspunkt == "morgen":
        print("Drikkevalg: Appelsinjuice")
    else:
        print("Drikkevalg: Brus")
else:
    if tidspunkt == "morgen":
        print("Drikkevalg: Kaffe")
    else:
        print("Drikkevalg: Vann")
        
#Eksempel 2:

vær = "sol"
tid = "dag"

if vær == "sol":
    if tid == "dag":
        print("Det er dagtid, husk solkrem!")
    else:
        print("Det er natt, nyt den klare himmelen!")
elif vær == "regn":
    if tid == "dag":
        print("Det er dagtid, ta med paraply!")
    else:
        print("Det er natt, ta med regnjakke!")
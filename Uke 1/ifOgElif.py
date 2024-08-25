score = 95

if score >= 90:
    print("Karakter: A")
if score >= 80:
    print("Karakter: B")
if score >= 70:
    print("Karakter: C")
if score >= 60:
    print("Karakter: D")
else:
    print("Karakter: F")
    
#Hva er feil her? Hvordan fikser man det?

#Bruk av "elif" forsikrer at bare én av betingelsene i en kjede av betingelser vil bli utført.
#Når vi bare bruker "if"-uttalelser, risikerer vi at flere betingelser evalueres,
#noe som kan føre til feilaktige resultater.

age = 15

if age < 13:
    print("Du er et barn.")
elif age < 18:
    print("Du er en tenåring.")
elif age < 65:
    print("Du er en voksen.")
else:
    print("Du er en senior.")
    
#Dette er riktig bruk av if og elif!

temperatur = 25

if temperatur < 10:
    print("Det er kaldt.")
if temperatur >= 10:
    print("Det er moderat.")
if temperatur >= 20:
    print("Det er varmt.")
    
#Hva er feil i dette tilfellet?

temperatur = 25

if temperatur < 10:
    print("Det er kaldt.")
elif temperatur >= 20:
    print("Det er varmt.")
elif temperatur >= 10:
    print("Det er moderat.")

#Viktig å følge med på rekkefølgen når man bruker elif slik.

#Dette er en annen mulig løsning, men raskere i løsningen over (særlig når man lager flere if setninger):

temperatur = 25

if temperatur < 10:
    print("Det er kaldt.")
if temperatur >= 10 and temperatur < 20:
    print("Det er moderat.")
if temperatur >= 20:
    print("Det er varmt.")
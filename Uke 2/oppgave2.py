def meny():
    print("-------MENY-------")
    print("1. sjekk saldo")
    print("2. ta ut penger")
    print("3. sett inn penger")
    print("4. avslutt")
    print("skriv inn ønsket tall")

def sjekkSaldo():
    print(f"Saldoen din er: {saldo}")

saldo = 0
svar = 0

while svar != "4":
    meny()
    svar = input(">")
    if svar == "1":
        sjekkSaldo()
    elif svar == "2":
        print("Hvor mye penger vil du ta ut?")
        sum = int(input(">"))
        saldo -= sum
    elif svar == "3":
        print("Hvor mye penger vil du sette inn?")
        sum = int(input(">"))
        saldo += sum
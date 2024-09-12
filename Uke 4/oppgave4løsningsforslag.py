inp = int(input("Skriv inn et tall: "))
total = inp

while inp != 10:
    inp = int(input("Skriv inn et tall: "))
    total += inp

print(f"Totale summen ble: {total}")
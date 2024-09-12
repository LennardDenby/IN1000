total = 0
inp = 0

while inp != 10:
    inp = int(input("Skriv inn et tall: "))
    if inp != 10:
        total += inp

print(f"Totale summen ble: {total}")
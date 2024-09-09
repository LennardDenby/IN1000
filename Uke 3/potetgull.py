potetgullNavn = ["larrys", "kims", "sørlandschips", "maarud"]

valg = input("Skriv inn chipps: ").lower()

if valg in potetgullNavn:
    print("Gjenkjent")
else:
    print("Det forstår jeg ikke")
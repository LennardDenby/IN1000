telefonbok = {
    "Arne"     : 22334455,
    "Lisa"     : 95959595,
    "Jonas"    : 97959795,
    "Peder"    : 12345678,
}
navn = input("Skriv in et navn: ")

if navn in telefonbok:
    print(telefonbok[navn])
else:
    nummer = int(input(f"Skriv inn telefonnummer til {navn}: "))
    telefonbok[navn] = nummer

print(telefonbok)
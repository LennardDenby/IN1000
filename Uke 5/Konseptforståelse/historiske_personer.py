fil = open("historiske_personer.txt", "r")
fil2 = open("oppdatrt_historiske_personer.txt", "w")

personer = []

for linje in fil:
    personer.append(linje.strip())

navn = input("Skriv inn en historisk person: ")
personer.append(navn)

for person in personer:
    fil2.write(person+"\n")


fil.close()
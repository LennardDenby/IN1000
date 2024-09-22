def gruppeOppmøte(filnavn):
    fil = open(filnavn)
    linje = fil.readline()
    
    grupper = linje.strip().split(";")
    
    for i in range(11):
        linje = fil.readline()

    oppmøte = linje.strip().split(";")
    
    for i in range(len(oppmøte)):
        if int(oppmøte[i]) >= 20:
            print(f"Gruppe {grupper[i]} hadde mer enn 20 oppmøte i uke 11")
            

gruppeOppmøte("oppmøte.txt") #Dette er en prosedyre, ikke en funksjon
#Finnes det en bedre løsning?
def siHei():
    print("Hei")
    
siHei() #<-- prosedyre kall

def sumerTall():
    tall1 = int(input("Skriv et tall: "))
    tall2 = int(input("Skriv et til tall: "))
    print(tall1 + tall2)

sumerTall()

tall = 13

def gjorNoe():
    tall += 3 #<-- kan ikke aksesere en "global" variabel
    print(tall)

gjorNoe()




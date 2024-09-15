liste = [0,0,1,2,0,3,0,0,4,0]

while liste[0] == 0:
    liste.pop(0)

while liste[-1] == 0:
    liste.pop()

print(liste)
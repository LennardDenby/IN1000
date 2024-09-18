fil = open("historiske_personer.txt")
personer = []

for linje in fil:
    personer.append(linje.strip())

fil.close()

print(personer)

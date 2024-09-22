fil = open("tall.txt", "r")

summen = 0

for linje in fil:
    tall = int(linje.strip())
    summen += tall

fil.close()
print(summen)